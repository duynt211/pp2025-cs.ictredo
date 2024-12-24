def input_student():
    stdnt_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter date of birth (DD/MM/YYYY): ")
    return stdnt_id, name, dob


def input_course():
    crs_id = input("Enter course ID: ")
    title = input("Enter course title: ")
    credits = int(input("Enter course credits: "))
    return crs_id, title, credits


def input_marks(students):
    marks = {}
    for student in students:
        while True:
            try:
                mark = float(input(f"Enter mark for {student.name}: "))
                marks[student.stdnt_id] = mark
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return marks
