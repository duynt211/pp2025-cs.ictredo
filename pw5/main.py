from domains.student import Stdnt
from domains.course import Crs
from domains.mark_manager import MrkMgr
import input as inp
import output as out
import os
import gzip
import pickle


# Save data to compressed file
def save_data_to_file(filename, data):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(data, f)


# Load data from compressed file
def load_data_from_file(filename):
    if os.path.exists(filename):
        with gzip.open(filename, 'rb') as f:
            return pickle.load(f)
    return None


def main():
    """
    Main function for managing the student marks system.
    """
    filename = 'students.dat'

    # Load existing data if file exists
    data = load_data_from_file(filename)
    if data:
        mgr = data['manager']
        print("Data loaded successfully from students.dat.")
    else:
        mgr = MrkMgr()  # Create a new Mark Manager instance

    while True:
        # Display the menu
        print("\nWelcome to the Student Marks Management System")
        print("1. Set the number of students and add their information")
        print("2. Add a single student")
        print("3. Set the number of courses and add course details")
        print("4. Add a single course")
        print("5. Add marks for a specific course")
        print("6. View the course list")
        print("7. View the student list")
        print("8. View student marks for a specific course")
        print("9. Show GPA for all students")
        print("10. Exit the application")

        choice = input("Please choose an option: ")

        try:
            if choice == '1':
                # Add multiple students
                n_students = int(input("How many students would you like to register? "))
                for _ in range(n_students):
                    stdnt_id, name, dob = inp.input_student()
                    mgr.add_student(Stdnt(stdnt_id, name, dob))
            elif choice == '2':
                # Add a single student
                stdnt_id, name, dob = inp.input_student()
                mgr.add_student(Stdnt(stdnt_id, name, dob))
            elif choice == '3':
                # Add multiple courses
                n_courses = int(input("How many courses would you like to add? "))
                for _ in range(n_courses):
                    crs_id, title, credits = inp.input_course()
                    mgr.add_course(Crs(crs_id, title, credits))
            elif choice == '4':
                # Add a single course
                crs_id, title, credits = inp.input_course()
                mgr.add_course(Crs(crs_id, title, credits))
            elif choice == '5':
                # Add marks for a specific course
                course_id = input("Enter course ID: ")
                course = mgr.find_course_by_id(course_id)
                if course:
                    marks = inp.input_marks(mgr.list_students())
                    for stdnt_id, mark in marks.items():
                        course.add_mark(stdnt_id, mark)
                else:
                    print("Course not found.")
            elif choice == '6':
                # View the course list
                out.show_courses(mgr.list_courses())
            elif choice == '7':
                # View the student list
                out.show_students(mgr.list_students())
            elif choice == '8':
                # View marks for a specific course
                course_id = input("Enter course ID to view marks: ")
                course = mgr.find_course_by_id(course_id)
                if course:
                    out.show_marks(course, mgr.list_students())
                else:
                    print("Course not found.")
            elif choice == '9':
                # Calculate and show GPA
                mgr.calculate_gpa()
                out.show_gpa(mgr.list_students())
            elif choice == '10':
                # Save data and exit the program
                data = {'manager': mgr}
                save_data_to_file(filename, data)
                print("Data saved successfully. Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Input error: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
