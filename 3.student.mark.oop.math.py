import math


class Stdnt:
    def __init__(self, stdnt_id, nm, dob):
        self.__stdnt_id = stdnt_id
        self.__nm = nm
        self.__dob = dob
        self.__gpa = 0.0

    @property
    def stdnt_id(self):
        return self.__stdnt_id

    @property
    def nm(self):
        return self.__nm

    @property
    def dob(self):
        return self.__dob

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    def __str__(self):
        return f"ID: {self.__stdnt_id}, Name: {self.__nm}, DOB: {self.__dob}, GPA: {self.__gpa:.2f}"


class Crs:
    def __init__(self, crs_id, ttl, credits):
        self.__crs_id = crs_id
        self.__ttl = ttl
        self.__credits = credits
        self.__mrks = {}

    @property
    def crs_id(self):
        return self.__crs_id

    @property
    def ttl(self):
        return self.__ttl

    @property
    def credits(self):
        return self.__credits

    def add_mrk(self, stdnt_id, mrk):
        # Round down to 1 decimal place
        mrk = math.floor(mrk * 10) / 10.0
        if 0 <= mrk <= 20:
            self.__mrks[stdnt_id] = mrk
        else:
            raise ValueError("Mark must be between 0 and 20.")

    def get_mrks(self):
        return self.__mrks

    def __str__(self):
        return f"Course ID: {self.__crs_id}, Title: {self.__ttl}, Credits: {self.__credits}"


class MrkMgr:
    def __init__(self):
        self.__stdnts = []
        self.__crses = []

    def input_num_of_stdnts(self):
        try:
            n_stdnts = int(input("How many students would you like to register? "))
            if n_stdnts > 0:
                return n_stdnts
            else:
                print("Please provide a positive number.")
                return self.input_num_of_stdnts()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.input_num_of_stdnts()

    def input_stdnt_info(self):
        stdnt_id = input("Enter the student ID: ")
        nm = input("Enter the full name of the student: ")
        dob = input("Enter the date of birth (DD/MM/YYYY): ")
        self.__stdnts.append(Stdnt(stdnt_id, nm, dob))

    def input_num_of_crses(self):
        try:
            n_crses = int(input("How many courses would you like to add? "))
            if n_crses > 0:
                return n_crses
            else:
                print("Please provide a positive number.")
                return self.input_num_of_crses()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.input_num_of_crses()

    def input_crs_info(self):
        crs_id = input("Enter the course ID: ")
        ttl = input("Enter the course title: ")
        credits = int(input("Enter the course credits: "))
        self.__crses.append(Crs(crs_id, ttl, credits))

    def input_mrks_for_crs(self):
        crs_id = input("Enter the course ID: ")
        course = self.__find_crs_by_id(crs_id)
        if course:
            for stdnt in self.__stdnts:
                try:
                    mrk = float(input(f"Enter mark for {stdnt.nm}: "))
                    course.add_mrk(stdnt.stdnt_id, mrk)
                except ValueError as e:
                    print(e)
        else:
            print("Course not found.")

    def show_stdnt_mrks_for_crs(self):
        crs_id = input("Enter the course ID to view marks: ")
        course = self.__find_crs_by_id(crs_id)
        if course:
            mrks = course.get_mrks()
            print(f"Marks for course {course.ttl}:")
            for stdnt_id, mrk in mrks.items():
                stdnt = self.__find_stdnt_by_id(stdnt_id)
                if stdnt:
                    print(f"{stdnt.nm} (ID: {stdnt.stdnt_id}): {mrk}")
        else:
            print("Course not found.")

    def list_crses(self):
        if not self.__crses:
            print("No courses have been added yet.")
        else:
            print("Available courses:")
            for course in self.__crses:
                print(course)

    def list_stdnts(self):
        if not self.__stdnts:
            print("No students have been registered yet.")
        else:
            print("Registered students:")
            for stdnt in self.__stdnts:
                print(stdnt)

    def calc_gpa(self):
        for stdnt in self.__stdnts:
            total_weighted = 0
            total_credits = 0
            for course in self.__crses:
                if stdnt.stdnt_id in course.get_mrks():
                    total_weighted += course.get_mrks()[stdnt.stdnt_id] * course.credits
                    total_credits += course.credits
            stdnt.gpa = total_weighted / total_credits if total_credits > 0 else 0

    def show_gpa(self):
        self.calc_gpa()
        print("GPA for all students:")
        for stdnt in self.__stdnts:
            print(f"{stdnt.nm} (ID: {stdnt.stdnt_id}): GPA = {stdnt.gpa:.2f}")

    def __find_crs_by_id(self, crs_id):
        for crs in self.__crses:
            if crs.crs_id == crs_id:
                return crs
        return None

    def __find_stdnt_by_id(self, stdnt_id):
        for stdnt in self.__stdnts:
            if stdnt.stdnt_id == stdnt_id:
                return stdnt
        return None

    def run(self):
        while True:
            print("\nWelcome to the Student Marks Management System")
            print("1. Set the number of students")
            print("2. Add student information")
            print("3. Set the number of courses")
            print("4. Add course details")
            print("5. Add marks for a specific course")
            print("6. View the course list")
            print("7. View the student list")
            print("8. View student marks for a specific course")
            print("9. Show GPA for all students")
            print("10. Exit the application")

            choice = input("Please choose an option: ")

            if choice == '1':
                n_stdnts = self.input_num_of_stdnts()
                for _ in range(n_stdnts):
                    self.input_stdnt_info()
            elif choice == '2':
                self.input_stdnt_info()
            elif choice == '3':
                n_crses = self.input_num_of_crses()
                for _ in range(n_crses):
                    self.input_crs_info()
            elif choice == '4':
                self.input_crs_info()
            elif choice == '5':
                self.input_mrks_for_crs()
            elif choice == '6':
                self.list_crses()
            elif choice == '7':
                self.list_stdnts()
            elif choice == '8':
                self.show_stdnt_mrks_for_crs()
            elif choice == '9':
                self.show_gpa()
            elif choice == '10':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    mgr = MrkMgr()
    mgr.run()


if __name__ == "__main__":
    main()
