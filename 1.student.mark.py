#1.stud.mrk.py 

# Global vars to store data
stds = []
crses = []
mrks = {}

# Input funcs
def inp_num_stds():
    while True:
        try:
            n_stds = int(input("How many students would you like to enter? "))
            if n_stds > 0:
                return n_stds
            else:
                print("Please enter a positive number of students.")
        except ValueError:
            print("Please enter a valid number.")

def inp_std_info():
    std_id = input("Provide the student ID: ")
    std_name = input("Enter the student's full name: ")
    std_dob = input("Input the student's date of birth (DD/MM/YYYY): ")
    stds.append((std_id, std_name, std_dob))
    print(f"Student {std_name} has been successfully added.")

def inp_num_crses():
    while True:
        try:
            n_crses = int(input("How many courses do you want to add? "))
            if n_crses > 0:
                return n_crses
            else:
                print("The number of courses should be a positive integer.")
        except ValueError:
            print("Please input a valid number.")

def inp_crs_info():
    crs_id = input("Enter the unique course ID: ")
    crs_name = input("Enter the course title: ")
    crses.append((crs_id, crs_name))
    mrks[crs_id] = {}
    print(f"The course {crs_name} has been successfully added.")

def inp_mrks_for_crs():
    if not crses:
        print("No courses found. Please add some courses first.")
        return

    print("These are the available courses:")
    for crs_id, crs_name in crses:
        print(f"{crs_id}: {crs_name}")

    sel_crs_id = input("Please enter the course ID where you want to add marks: ")
    if sel_crs_id not in mrks:
        print("The provided course ID is invalid.")
        return

    if not stds:
        print("No students are registered. Please add students first.")
        return

    print("These are the available students:")
    for std_id, std_name, _ in stds:
        print(f"{std_id}: {std_name}")
    while True:
        try:
            mark = float(input(f"Provide the mark for {std_name}: "))
            if 0 <= mark <= 20:
                mrks[sel_crs_id][std_id] = mark
                break
            else:
                print("The mark must be between 0 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("The marks have been successfully added.")

# Listing funcs
def lst_crses():
    if not crses:
        print("There are no courses available.")
    else:
        print("Courses list:")
        for crs_id, crs_name in crses:
            print(f"{crs_id}: {crs_name}")

def lst_stds():
    if not stds:
        print("No students have been registered.")
    else:
        print("Registered students:")
        for std_id, std_name, std_dob in stds:
            print(f"{std_id}: {std_name}, DoB: {std_dob}")

def show_std_mrks_for_crs():
    if not crses:
        print("Please add courses before checking marks.")
        return

    print("These are the available courses:")
    for crs_id, crs_name in crses:
        print(f"{crs_id}: {crs_name}")

    sel_crs_id = input("Enter the course ID to view marks: ")
    if sel_crs_id not in mrks:
        print("The course ID is incorrect.")
        return

    if not mrks[sel_crs_id]:
        print("No marks have been recorded for this course.")
    else:
        print(f"Marks for course {sel_crs_id}:")
        for std_id, mark in mrks[sel_crs_id].items():
            std_name = next(name for id, name, _ in stds if id == std_id)
            print(f"{std_name} (ID: {std_id}): {mark}")

# Main func to run the program
def main():
    while True:
        print("\nWelcome to the Student Mark Management System")
        print("1. Specify the number of students")
        print("2. Enter student details")
        print("3. Specify the number of courses")
        print("4. Enter course details")
        print("5. Input marks for a specific course")
        print("6. View list of courses")
        print("7. View list of students")
        print("8. Display student marks for a course")
        print("9. Exit the program")

        ch = input("What would you like to do? Please enter your choice: ")

        if ch == '1':
            n_stds = inp_num_stds()
            for _ in range(n_stds):
                inp_std_info()
        elif ch == '2':
            inp_std_info()
        elif ch == '3':
            n_crses = inp_num_crses()
            for _ in range(n_crses):
                inp_crs_info()
        elif ch == '4':
            inp_crs_info()
        elif ch == '5':
            inp_mrks_for_crs()
        elif ch == '6':
            lst_crses()
        elif ch == '7':
            lst_stds()
        elif ch == '8':
            show_std_mrks_for_crs()
        elif ch == '9':
            print("Goodbye! Exiting the program now.")
            break
        else:
            print("Invalid option. Please select a valid choice.")

if __name__ == "__main__":
    main()
