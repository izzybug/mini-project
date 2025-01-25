def main_menu():
    while True:
        print("School Management System")
        print("1. View list of students")
        print("2. View list of lecturers")
        print("3. View list of courses")
        print("4. Generate report")
        print("5. Accountant System")
        print("6. Exit")
        choice = input("Make a choice (1-6):")
        if choice == "1":
            print ("1. Check student exist or not")
            print ("2. Other")
            choice2 = input ("1 or 2:")
            if choice2 == "1":
                student()
            else:
                studentSystem()
        elif choice == "2":
            print("1. Check lecturer exist or not")
            print("2. Other")
            choice2 = input("1 or 2:")
            if choice2 == "1":
                lecturer()
            else:
                lecturerSystem()
        elif choice == "3":
            courses()
        elif choice == '4':
            print ("1. Student Report")
            print ("2. Course Report")
            choices = input("Choose between 1 or 2:")
            if choices == "1":
                generateStudentReport()
            else:
                generateCourseReport()
        elif choice == "5":
            accountantSystem()
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again")

def ifStudentExists(id,student_list):
    for record in student_list:
        if record[1] == id:
            return True
    else:
        return False
def ifNameIsValid(name):
    if name.isalpha():
        return True
    else:
        return False

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip().split(",") for line in file]
    except FileNotFoundError:
        print(f"{filename} not found!")
        return []


def student():
    student_list = read_file("student.txt")
    ID = input ("Enter student ID to check if exits:")
    if ifStudentExists(ID, student_list):
        print ("Student exits!")
        print (student_list)
    else:
        print ("Student ID does not exist!")
        name = input ("Enter student name:")
        if not ifNameIsValid(name):
            print ("Invalid name, please enter alphabetical character only.")
            return

        question = input("Do you want to add a student? (yes/no):")
        if question.lower() == "yes":
            new_department = input("Enter student department (graduate/undergraduate/international):")
            department = [new_department]
            with open("department.txt", "a") as  destfile:
                destfile.write(",".join(department) + "\n")
            new_student = [name, ID, new_department]
            student_list.append(new_student)
            with open("student.txt", "a") as destfile:
                destfile.write(",".join(new_student) + "\n")
                print("Student added successfully!")
                print (student_list)

        else:
            print ("Student not added")

def studentSystem():
    while True:
        print("1.View available modules")
        print("2.Enroll in modules")
        print("3.View Grades")
        print("4.View attendance")
        print("5.Unenroll from module")
        choice= input("Enter your choice: ")
        if choice == "1":
            viewmodules()
        elif choice=="2":
            enrollinmodule()
        elif choice == "3":
            viewgrades()
        elif choice == "4":
            viewattendance()
        elif choice == "5":
            unenrollfrommodule()
        else:
            break


def viewmodules():
    print("Please enter your course code")
    input("course code: ")
    file=open("modules.txt")
    for line in file:
        if True:
           print(line.strip())
        else:
            print("Inexisting course code")
    return menu



def enrollinmodule():
    print("Do you want to enroll in this module")
    print("1.Yes")
    print("2.No")
    choice = input(": ")
    if choice == "1":
        print("Enrollement successful")
        file=open("modules.txt","a")
        file.write("student enrolled in module\n")
    else:
        print ("Not enrolled")
    return menu


def viewgrades():
    print("Enter your credentials")
    input(": ")
    if True:
        print("Your grade:+grade")
    else:
        print("Inexisting credentials")
    return menu


def viewattendance():
    print("Enter your credentails")
    input(": ")
    if True:
        print("Your attendance:+attendance")
    else:
        print("Inexisting credentials")
    return menu



def unenrollfrommodule():
    print("Please enter module name")
    input("name:")
    file=open("modules.txt", "a")
    for index,line in file:
        if line[0] == index:
           del [index]
    return menu



def ifLectureExists(course,lecturer_list):
    for record in lecturer_list:
        if record[1] == course:
            return True
    else:
        return False
def ifLecturerIsValid(name):
    if name.isalpha():
        return True
    else:
        return False

def lecturer():
    lecturer_list = read_file("lecturer.txt")
    name = input ("Enter lecturer name to check if exist:")
    if ifLectureExists(course, lecturer_list):
        print ("Lecturer exist!")
    else:
        print ("Lecturer not found!")
        course = input ("Enter course name:")
        if not ifLecturerIsValid(course):
            print ("Invalid course, please enter alphabatical character or an existing course name!")
            return

        question2 = input("Would you like to this lecturer? (yes/no):")
        if question2.lower() == "yes":
            new_lecturer = [name, course]
            with open("lecturer.txt", "a") as destfile:
                destfile.write(",".join(new_lecturer) + "\n")
                lecturer_list.append(new_lecturer)
                print(lecturer_list)
                print("Lecturer added succesfully!")
        else:
            print ("Lecturer not added!")

def lecturerSystem():
    file1 = open('DIP. txt', 'r+')
    file2 = open('IVRARM. txt', 'r+')
    file3 = open('DGTIN. txt', 'r+')
    english = file1.readlines()
    maths = file2.readlines()
    science = file3.readlines()
    found = "False"
    leave = False
    loop = True
    position = 0
    counter = 0
    # list items add later, placeholders
    module1 = ["DIP", "IVRARM"]
    module2 = ["IVRARM", "DGTIN"]
    student1 = []
    student2 = []
    student3 = []
    attendance1 = []
    attendance2 = []
    attendance3 = []
    grade1 = []
    grade2 = []
    grade3 = []
    # variables for related sections
    attendance_times = 0

    with open("DIP. txt", 'r') as e:
        e_lines = len(e.readlines())

    while counter < e_lines:
        student1.append(english[counter])
        counter = counter + 1
    counter = 0

    with open("IVRARM. txt", 'r+') as m:
        m_lines = len(m.readlines())

    while counter < m_lines:
        student2.append(maths[counter])
        counter = counter + 1
    counter = 0

    with open("DGTIN. txt", 'r') as s:
        s_lines = len(s.readlines())

    while counter < s_lines:
        student3.append(science[counter])
        counter = counter + 1
    counter = 0

    for i in range(e_lines):
        attendance1.append("absent")
        grade1.append("none")

    for i in range(m_lines):
        attendance2.append("absent")
        grade2.append("none")

    for i in range(s_lines):
        attendance3.append("absent")
        grade3.append("none")

    print("Welcome Lecturer")

    while leave == False:
        choice = input(
            "Would you like to\n1.View Modules\n2.Manage Grades\n3.View Students\n4.Take Attendance\n5.View Grades\nEnter:")
        # edited inputs to accept more types of inputs from user (including inside)
        # lecturer view their modules done?
        if choice == "1" or "view modules" in choice:
            while leave == False:
                # this line is temporary
                print(module1)
                # if username = lecturer1:
                # print (module1)
                # elif username = lecturer2:
                # print (module2)
                close = input("Do you want to exit? y/n\nEnter:")
                if close == "y":
                    leave = True
                elif close == "n":
                    leave = False
                    print("rerunning code")
        # lecturer edits grades done, added loops and error fixes
        elif choice == "2" or "manage" in choice:
            while leave == False:
                pick = input("1.DIP\n2.IVRARM\n3.DGTIN\nEnter:")
                if pick == "1" or pick == "DIP":
                    print(student1)
                    print(grade1)
                    name = input("Enter name of Student:")
                    name = name + "\n"
                    counter = 0
                    for i in range(len(student1)):
                        if student1[counter] == name:
                            position = counter
                            found = "True"
                        else:
                            counter = counter + 1
                            if counter == len(student1) - 1:
                                name = name.strip()
                            if counter == len(student1):
                                print("invalid input")
                                found = "False"
                    if found == "True":
                        g_action = input("1.Edit Grades\n2.Remove Grades\nEnter:")
                        if g_action == "1" or "edit" in g_action:
                            loop = True
                            new_grade = input("Enter new grade:")
                            while loop == True:
                                if new_grade.isdigit():
                                    grade1[position] = new_grade
                                    print(student1)
                                    print(grade1)
                                    loop = False
                                else:
                                    print("invalid input")
                                    new_grade = input("Enter new grade:")
                                    loop = True
                        elif g_action == "2" or "remove" in g_action:
                            grade1[position] = "none"
                            print(student1)
                            print(grade1)
                        else:
                            print("invalid input")
                    else:
                        print("try again")
                elif pick == "2" or pick == "IVRARM":
                    print(student2)
                    print(grade2)
                    name = input("Enter name of Student:")
                    name = name + "\n"
                    counter = 0
                    for i in range(len(student2)):
                        if student2[counter] == name:
                            position = counter
                            found = "True"
                        else:
                            counter = counter + 1
                            if counter == len(student2) - 1:
                                name = name.strip()
                            if counter == len(student2):
                                print("invalid input")
                                found = "False"
                    if found == "True":
                        g_action = input("1.Edit Grades\n2.Remove Grades\nEnter:")
                        if g_action == "1" or "edit" in g_action:
                            new_grade = input("Enter new grade:")
                            while loop == True:
                                if new_grade.isdigit():
                                    grade2[position] = new_grade
                                    print(student2)
                                    print(grade2)
                                    loop = False
                                else:
                                    print("invalid input")
                                    new_grade = input("Enter new grade:")
                                    loop = True
                        elif g_action == "2" or "remove" in g_action:
                            grade2[position] = "none"
                            print(student2)
                            print(grade2)
                        else:
                            print("invalid input")
                    else:
                        print("try again")
                elif pick == "3" or pick == "DGTIN":
                    print(student3)
                    print(grade3)
                    name = input("Enter name of Student:")
                    name = name + "\n"
                    counter = 0
                    for i in range(len(student3)):
                        if student3[counter] == name:
                            position = counter
                            found = "True"
                        else:
                            counter = counter + 1
                            if counter == len(student3) - 1:
                                name = name.strip()
                            if counter == len(student3):
                                print("invalid input")
                                found = "False"
                    if found == "True":
                        g_action = input("1.Edit Grades\n2.Remove Grades\nEnter:")
                        if g_action == "1" or "edit" in g_action:
                            new_grade = input("Enter new grade:")
                            while loop == True:
                                if new_grade.isdigit():
                                    grade3[position] = new_grade
                                    print(student3)
                                    print(grade3)
                                    loop = False
                                else:
                                    print("invalid input")
                                    new_grade = input("Enter new grade:")
                                    loop = True
                        elif g_action == "2" or "remove" in g_action:
                            grade3[position] = "none"
                            print(student3)
                            print(grade3)
                        else:
                            print("invalid input")
                    else:
                        print("try again")
                else:
                    print("invalid input")
                close = input("Do you want to exit? y/n\nEnter:")
                if close == "y":
                    leave = True
                elif close == "n":
                    leave = False
                    print("rerunning code")
        # views student done
        elif choice == "3" or "view students" in choice:
            while leave == False:
                # module names add later
                pick = input("1.DIP\n2.IVRARM\n3.DGTIN\nEnter:")
                if pick == "1" or pick == "DIP":
                    print(student1)
                elif pick == "2" or pick == "IVRARM":
                    print(student2)
                elif pick == "3" or pick == "DGTIN":
                    print(student3)
                else:
                    print("invalid input")

                close = input("Do you want to exit? y/n\n")
                if close == "y":
                    leave = True
                elif close == "n":
                    leave = False
                    print("rerunning code")
        # takes attendance, added loops and error fixes
        elif choice == "4" or "attendance" in choice:
            while leave == False:
                new = input("Take new attendance? y/n\nEnter:")
                loop = True
                while loop == True:
                    if new == "y":
                        attendance_times = attendance_times + 1
                        loop = False
                        print("loading new attendance...")
                        new = "y"
                    elif new == "n":
                        loop = False
                        print("loading attendance...")
                    else:
                        print("invalid input")
                        new = input("Take new attendance? y/n\nEnter:")
                pick = input("1.DIP\n2.IVRARM\n3.DGTIN\nEnter:")
                if pick == "1" or pick == "DIP":
                    if new == "y":
                        for i in range(e_lines):
                            attendance1.clear()
                            attendance1.append("absent")
                    print(student1)
                    print(attendance1)
                    name = input("Enter student name:")
                    name = name + "\n"
                    counter = 0
                    for i in range(len(student1)):
                        if student1[counter] == name:
                            position = counter
                            found = "True"
                        else:
                            counter = counter + 1
                            if counter == len(student1) - 1:
                                name = name.strip()
                            if counter == len(student1):
                                print("invalid input")
                                found = "False"
                    if found == "True":
                        status = input("1.present\n2.late\n3.absent\nEnter:")
                        if status == "1" or status == "present":
                            attendance1[position] = "present"
                            print(student1)
                            print(attendance1)
                        elif status == "2" or status == "late":
                            attendance1[position] = "late"
                            print(student1)
                            print(attendance1)
                        elif status == "3" or status == "absent":
                            attendance1[position] = "absent"
                            print(student1)
                            print(attendance1)
                        else:
                            print("invalid input")
                    else:
                        print("try again")
                elif pick == "2" or pick == "IVRARM":
                    if new == "y":
                        for i in range(m_lines):
                            attendance2.append("absent")
                    print(student2)
                    print(attendance2)
                    name = input("Enter student name:")
                    name = name + "\n"
                    counter = 0
                    for i in range(len(student2)):
                        if student2[counter] == name:
                            position = counter
                            found = "True"
                        else:
                            counter = counter + 1
                            if counter == len(student2) - 1:
                                name = name.strip()
                            if counter == len(student2):
                                print("invalid input")
                                found = "False"
                    if found == "True":
                        status = input("1.present\n2.late\n3.absent\nEnter:")
                        if status == "1" or status == "present":
                            attendance2[position] = "present"
                            print(student2)
                            print(attendance2)
                        elif status == "2" or status == "late":
                            attendance2[position] = "late"
                            print(student2)
                            print(attendance2)
                        elif status == "3" or status == "absent":
                            attendance2[position] = "absent"
                            print(student2)
                            print(attendance2)
                        else:
                            print("invalid input")
                    else:
                        print("try again")
                elif pick == "3" or pick == "DGTIN":
                    if new == "y":
                        for i in range(s_lines):
                            attendance3.append("absent")
                    print(student3)
                    print(attendance3)
                    name = input("Enter student name:")
                    name = name + "\n"
                    counter = 0
                    for i in range(len(student3)):
                        if student3[counter] == name:
                            position = counter
                            found = "True"
                        else:
                            counter = counter + 1
                            if counter == len(student3) - 1:
                                name = name.strip()
                            if counter == len(student3):
                                print("invalid input")
                                found = "False"
                    if found == "True":
                        status = input("1.present\n2.late\n3.absent\nEnter:")
                        if status == "1" or status == "present":
                            attendance3[position] = "present"
                            print(student3)
                            print(attendance3)
                        elif status == "2" or status == "late":
                            attendance3[position] = "late"
                            print(student3)
                            print(attendance3)
                        elif status == "3" or status == "absent":
                            attendance3[position] = "absent"
                            print(student3)
                            print(attendance3)
                        else:
                            print("invalid input")
                    else:
                        print("try again")
                else:
                    print("invalid input")

                close = input("Do you want to exit? y/n\n")
                if close == "y":
                    leave = True
                elif close == "n":
                    leave = False
                    print("rerunning code")
        # view the grades
        elif choice == "5" or "view grades" in choice:
            while leave == False:
                pick = input("1.DIP\n2.IVRARM\n3.DGTIN\nEnter:")
                if pick == "1" or pick == "DIP":
                    print(student1)
                    print(grade1)
                elif pick == "2" or pick == "IVRARM":
                    print(student2)
                    print(grade2)
                elif pick == "3" or pick == "DGTIN":
                    print(student3)
                    print(grade3)
                else:
                    print("invalid input")
                close = input("Do you want to exit? y/n\nEnter:")
                if close == "y":
                    leave = True
                elif close == "n":
                    leave = False
                    print("rerunning code")
        else:
            print("invalid input")
        # exit code
        close = input("Do you want to exit lecturer menu? y/n\nEnter:")
        if close == "y":
            leave = True
        elif close == "n":
            leave = False
            print("rerunning code")

def ifCourseExists(code ,course_list):
    for record in course_list:
        if record[1] == code:
            return True
    else:
        return False
def ifCourseIsValid(course_name):
    if course_name.isalpha():
        return True
    else:
        return False

def courses():
    course_list = read_file("course.txt")
    code = input ("Enter course code to check if exits:")
    if ifCourseIsValid(code, course_list):
        print ("Course code not found:")
        course_name = input ("Enter course name:")
        if not ifCourseIsValid(course_name):
            print ("Invalid name, please enter alphabatical character or enter a exist course name!")
            return

        question3 = input ("Do you want to add this course? (yes/no):")
        if question3.lower() == "yes":
            credit = input ("Enter course credit:")
            new_courses = [course_name, code, str(credit)]
            course = [new_courses]
            with open("courses.txt", "a") as destfile:
                destfile.write(",".join(course) + "\n")
            course_list.append(new_courses)
            with open("course.txt", "a") as course_name:
                course_name.write(",".join(new_courses) + "\n")
                print("Course added successfully!")
        else:
            print ("Course not added!")

def generateStudentReport():
    department = read_file('department.txt')
    student_list = read_file ('student.txt')
    total_student = len(student_list)
    undergraduate_student = 0
    graduate_student = 0
    international_student = 0



    for student in student_list:
        if len(student) < 2:
            print("Invalid student data format!")
            continue

        if department == "undergraduate":
            undergraduate_student += 1
        elif department == "graduate":
            graduate_student += 1
        elif department == "international":
            international_student += 1
        else:
            print ("Invalid input!")

            report = input("Total student =", total_student) + "\n"
            print (report)
            break

def generateCourseReport():
    course = read_file('courses.txt')
    course_list = read_file('course.txt')
    total_course = len(course_list)
    DIP_student = 0
    IVRAM_student = 0
    DGTIN_student = 0

    for course in course_list:
        if len(course_list) < 2:
            print("Invalid input!")
            continue

        if course == "DIP":
            DIP_student += 1
        elif course == "IVRAM":
            IVRAM_student += 1
        elif course == "DGTIN":
            DGTIN_student += 1
        else:
            print("Invalid input!")

            report = input("Total course =", course_list) + "\n"
            print (report)
            break
def accountantSystem():
    while True:
        print("\nAccountant System")
        print("1. Record Tuition Fees")
        print("2. View Outstanding Fees")
        print("3. Update Payment Records")
        print("4. Issue Fee Receipt")
        print("5. View Financial Summary")
        print("6. Return to Main Menu")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            recordTuitionFees()
        elif choice == "2":
            viewOutstandingFees()
        elif choice == "3":
            updatePaymentRecords()
        elif choice == "4":
            issueFeeReceipt()
        elif choice == "5":
            viewFinancialSummary()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def recordTuitionFees():
    student_list = read_file("student.txt")
    fee_records = read_file("fees.txt")
    
    student_id = input("Enter student ID: ")
    if not ifStudentExists(student_id, student_list):
        print("Student ID does not exist!")
        return
    
    try:
        amount = float(input("Enter payment amount: "))
        payment_date = input("Enter payment date (YYYY-MM-DD): ")
        semester = input("Enter semester (e.g., Fall 2024): ")
        
        fee_record = [student_id, str(amount), payment_date, semester]
        with open("fees.txt", "a") as destfile:
            destfile.write(",".join(fee_record) + "\n")
        print("Payment recorded successfully!")
        
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def viewOutstandingFees():
    student_list = read_file("student.txt")
    fee_records = read_file("fees.txt")
    
    print("\nStudents with Outstanding Fees:")
    print("--------------------------------")
    
    total_fees = {}  # Dictionary to store total fees per student
    paid_fees = {}   # Dictionary to store paid fees per student
    
    # Set default total fees for all students
    for student in student_list:
        if len(student) > 1:  # Ensure valid student record
            total_fees[student[1]] = 10000  # Default total fees per semester
            paid_fees[student[1]] = 0
    
    # Calculate paid fees
    for record in fee_records:
        if len(record) > 1:  # Ensure valid fee record
            student_id = record[0]
            amount = float(record[1])
            paid_fees[student_id] = paid_fees.get(student_id, 0) + amount
    
    # Display outstanding fees
    for student_id in total_fees:
        outstanding = total_fees[student_id] - paid_fees.get(student_id, 0)
        if outstanding > 0:
            print(f"Student ID: {student_id}")
            print(f"Outstanding Amount: ${outstanding:.2f}")
            print("--------------------------------")

def updatePaymentRecords():
    fee_records = read_file("fees.txt")
    
    student_id = input("Enter student ID: ")
    payment_date = input("Enter payment date to update (YYYY-MM-DD): ")
    
    found = False
    updated_records = []
    
    for record in fee_records:
        if len(record) > 2 and record[0] == student_id and record[2] == payment_date:
            found = True
            try:
                new_amount = float(input("Enter new payment amount: "))
                record[1] = str(new_amount)
                print("Payment record updated successfully!")
            except ValueError:
                print("Invalid amount. Update cancelled.")
                return
        updated_records.append(record)
    
    if not found:
        print("No matching payment record found!")
        return
    
    with open("fees.txt", "w") as destfile:
        for record in updated_records:
            destfile.write(",".join(record) + "\n")

def issueFeeReceipt():
    student_list = read_file("student.txt")
    
    student_id = input("Enter student ID: ")
    if not ifStudentExists(student_id, student_list):
        print("Student ID does not exist!")
        return
    
    receipt_date = input("Enter receipt date (YYYY-MM-DD): ")
    amount = input("Enter amount paid: ")
    payment_method = input("Enter payment method: ")
    
    receipt = f"""
    FEE RECEIPT
    ---------------------
    Date: {receipt_date}
    Student ID: {student_id}
    Amount Paid: ${amount}
    Payment Method: {payment_method}
    ---------------------
    """
    
    receipt_filename = f"receipt_{student_id}_{receipt_date}.txt"
    with open(receipt_filename, "w") as destfile:
        destfile.write(receipt)
    print(f"Receipt generated and saved as {receipt_filename}")

def viewFinancialSummary():
    fee_records = read_file("fees.txt")
    student_list = read_file("student.txt")
    
    total_expected = len(student_list) * 10000  # Assuming $10000 per student
    total_collected = 0
    
    for record in fee_records:
        if len(record) > 1:
            total_collected += float(record[1])
    
    total_outstanding = total_expected - total_collected
    
    print("\nFinancial Summary")
    print("------------------------")
    print(f"Total Expected Fees: ${total_expected:.2f}")
    print(f"Total Collected Fees: ${total_collected:.2f}")
    print(f"Total Outstanding Fees: ${total_outstanding:.2f}")
    print(f"Collection Rate: {(total_collected/total_expected*100):.1f}%")

# Start the program
main_menu()