import pandas as pd
from pulp import *

def create_picking_optimization_model(data_df):
    # Create the model
    model = LpProblem("Picking_Time_Optimization", LpMinimize)
    
    # Process input data
    locations = data_df['l'].unique()
    skus = data_df['s'].unique()
    
    # Parameters
    hi = dict(zip(data_df['l'], data_df['hi']))  # Storage location distances
    r = dict(zip(data_df['l'], data_df['r']))    # Fast pick to reserve distances
    qs = dict(zip(data_df['s'], data_df['qs']))  # SKU quantities in storage
    ds = dict(zip(data_df['s'], data_df['ds']))  # SKU demands
    ni = dict(zip(data_df['l'], data_df['ni']))  # Location numbers
    i_distance = dict(zip(data_df['s'], data_df['i (m)']))  # Distance for replenishment
    
    # Decision Variables
    yist = LpVariable.dicts("assign",
                           ((s, i) for s in skus for i in locations),
                           cat='Binary')
    
    zk = LpVariable("total_distance", lowBound=0)
    
    # Objective Function: Minimize total picking time
    # Convert distance to time using i (detik) and zk (detik) columns
    avg_time_per_meter = data_df['i (detik)'].mean() / data_df['i (m)'].mean()
    model += zk * avg_time_per_meter
    
    # Constraints
    
    # 1. Each SKU must be assigned to exactly one location
    for s in skus:
        model += lpSum(yist[s,i] for i in locations) == 1
    
    # 2. Total distance calculation
    model += zk >= lpSum(hi[i] * yist[s,i] for s in skus for i in locations)
    
    # 3. Capacity constraints - ensure storage location can handle SKU quantity
    for i in locations:
        model += lpSum(qs[s] * yist[s,i] for s in skus) <= 1000  # Assuming max capacity of 1000
    
    # 4. Demand satisfaction
    for s in skus:
        model += lpSum(ds[s] * yist[s,i] for i in locations) >= ds[s]
    
    return model

def solve_and_analyze(model, data_df):
    # Solve the model
    solver = PULP_CBC_CMD(msg=False)
    model.solve(solver)
    
    # Process results
    results = {
        'status': LpStatus[model.status],
        'objective_value': value(model.objective),
        'assignments': {}
    }
    
    # Extract assignments
    for var in model.variables():
        if var.name.startswith('assign'):
            if var.value() == 1:
                # Parse variable name to get SKU and location
                parts = var.name.split('_')[1:]
                sku = parts[0]
                location = parts[1]
                results['assignments'][sku] = location
    
    return results

def main(csv_path):
    # Read data
    data_df = pd.read_csv(csv_path)
    
    # Create and solve model
    model = create_picking_optimization_model(data_df)
    results = solve_and_analyze(model, data_df)
    
    # Print results
    print("\nOptimization Results:")
    print(f"Status: {results['status']}")
    print(f"Total Picking Time: {results['objective_value']:.2f} seconds")
    print("\nSKU Assignments:")
    for sku, location in results['assignments'].items():
        print(f"SKU {sku} → Location {location}")
    
    return results

# Example usage
if __name__ == "__main__":
    results = main("Book12.csv")