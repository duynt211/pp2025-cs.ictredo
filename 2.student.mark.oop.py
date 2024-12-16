# 2.std.mrk.oop.py

class Stdnt:
    def __init__(self, stdnt_id, nm, dob):
        self.__stdnt_id = stdnt_id
        self.__nm = nm
        self.__dob = dob

    # Getter and Setter for stdnt_id
    @property
    def stdnt_id(self):
        return self.__stdnt_id

    @stdnt_id.setter
    def stdnt_id(self, val):
        self.__stdnt_id = val

    # Getter and Setter for nm
    @property
    def nm(self):
        return self.__nm

    @nm.setter
    def nm(self, val):
        self.__nm = val

    # Getter and Setter for dob
    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, val):
        self.__dob = val

    def __str__(self):
        return f"Student ID: {self.__stdnt_id}, Name: {self.__nm}, Date of Birth: {self.__dob}"


class Crs:
    def __init__(self, crs_id, ttl):
        self.__crs_id = crs_id
        self.__ttl = ttl
        self.__mrks = {}  # key: stdnt_id, value: mark

    # Getter and Setter for crs_id
    @property
    def crs_id(self):
        return self.__crs_id

    @crs_id.setter
    def crs_id(self, val):
        self.__crs_id = val

    # Getter and Setter for ttl
    @property
    def ttl(self):
        return self.__ttl

    @ttl.setter
    def ttl(self, val):
        self.__ttl = val

    # Methods to manage marks
    def add_mrk(self, stdnt_id, mrk):
        if 0 <= mrk <= 20:
            self.__mrks[stdnt_id] = mrk
            print(f"Successfully recorded mark {mrk} for student ID {stdnt_id} in course {self.__ttl}.")
        else:
            print("The mark must be between 0 and 20.")

    def get_mrks(self):
        return self.__mrks

    def __str__(self):
        return f"Course ID: {self.__crs_id}, Title: {self.__ttl}"


class MrkMgr:
    def __init__(self):
        self.__stdnts = []
        self.__crses = []

    # Methods to manage stdnts
    def input_num_of_stdnts(self):
        while True:
            try:
                n_stdnts = int(input("How many students would you like to register? "))
                if n_stdnts > 0:
                    return n_stdnts
                else:
                    print("Please provide a positive number of students.")
            except ValueError:
                print("Please enter a valid number.")

    def input_stdnt_info(self):
        stdnt_id = input("Enter the student ID: ")
        nm = input("Enter the full name of the student: ")
        dob = input("Enter the date of birth (DD/MM/YYYY): ")
        stdnt = Stdnt(stdnt_id, nm, dob)
        self.__stdnts.append(stdnt)
        print(f"Student {nm} has been added successfully.")

    def list_stdnts(self):
        if not self.__stdnts:
            print("No students have been registered yet.")
        else:
            print("List of registered students:")
            for stdnt in self.__stdnts:
                print(stdnt)

    # Methods to manage crses
    def input_num_of_crses(self):
        while True:
            try:
                n_crses = int(input("How many courses would you like to add? "))
                if n_crses > 0:
                    return n_crses
                else:
                    print("Please enter a positive number of courses.")
            except ValueError:
                print("Please provide a valid number.")

    def input_crs_info(self):
        crs_id = input("Enter the unique course ID: ")
        ttl = input("Enter the course title: ")
        crs = Crs(crs_id, ttl)
        self.__crses.append(crs)
        print(f"The course {ttl} has been added successfully.")

    def list_crses(self):
        if not self.__crses:
            print("No courses are available at the moment.")
        else:
            print("List of available courses:")
            for crs in self.__crses:
                print(crs)

    # Methods to manage mrks
    def input_mrks_for_crs(self):
        if not self.__crses:
            print("There are no courses available. Please add courses first.")
            return

        print("Here are the available courses:")
        for crs in self.__crses:
            print(crs)

        selected_crs_id = input("Please enter the course ID where you wish to record marks: ")
        crs = self.__find_crs_by_id(selected_crs_id)
        if not crs:
            print("Invalid course ID entered.")
            return

        if not self.__stdnts:
            print("No students are registered. Please add students first.")
            return

        print("Here are the registered students:")
        for stdnt in self.__stdnts:
            print(stdnt)

        stdnt_id = input("Enter the student ID to record their mark: ")
        stdnt = self.__find_stdnt_by_id(stdnt_id)
        if not stdnt:
            print("The student ID entered is invalid.")
            return

        while True:
            try:
                mrk = float(input(f"Enter the mark for {stdnt.nm}: "))
                crs.add_mrk(stdnt_id, mrk)
                break
            except ValueError:
                print("Please enter a valid numerical value.")

    def show_stdnt_mrks_for_crs(self):
        if not self.__crses:
            print("Please add courses before viewing marks.")
            return

        print("Here are the available courses:")
        for crs in self.__crses:
            print(crs)

        selected_crs_id = input("Enter the course ID to view the marks: ")
        crs = self.__find_crs_by_id(selected_crs_id)
        if not crs:
            print("Invalid course ID entered.")
            return

        mrks = crs.get_mrks()
        if not mrks:
            print("No marks have been recorded for this course.")
        else:
            print(f"Marks for course {crs.ttl}:")
            for stdnt_id, mrk in mrks.items():
                stdnt = self.__find_stdnt_by_id(stdnt_id)
                if stdnt:
                    print(f"{stdnt.nm} (ID: {stdnt.stdnt_id}): {mrk}")

    # Helper methods
    def __find_stdnt_by_id(self, stdnt_id):
        for stdnt in self.__stdnts:
            if stdnt.stdnt_id == stdnt_id:
                return stdnt
        return None

    def __find_crs_by_id(self, crs_id):
        for crs in self.__crses:
            if crs.crs_id == crs_id:
                return crs
        return None

    # Main loop
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
            print("9. Exit the application")

            choice = input("What action would you like to perform? Please choose an option: ")

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
                print("Goodbye! Exiting the system now.")
                break
            else:
                print("Invalid selection. Please choose a valid option.")


def main():
    mgr = MrkMgr()
    mgr.run()


if __name__ == "__main__":
    main()
