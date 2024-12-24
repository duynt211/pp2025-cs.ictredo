from domains.student import Stdnt
from domains.course import Crs


class MrkMgr:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def add_student(self, student):
        self.__students.append(student)

    def add_course(self, course):
        self.__courses.append(course)

    def find_student_by_id(self, stdnt_id):
        return next((s for s in self.__students if s.stdnt_id == stdnt_id), None)

    def find_course_by_id(self, crs_id):
        return next((c for c in self.__courses if c.crs_id == crs_id), None)

    def list_students(self):
        return self.__students

    def list_courses(self):
        return self.__courses

    def calculate_gpa(self):
        for student in self.__students:
            total_weighted = 0
            total_credits = 0
            for course in self.__courses:
                marks = course.get_marks()
                if student.stdnt_id in marks:
                    total_weighted += marks[student.stdnt_id] * course.credits
                    total_credits += course.credits
            student.gpa = total_weighted / total_credits if total_credits > 0 else 0

    def get_marks_for_course(self, crs_id):
        course = self.find_course_by_id(crs_id)
        if not course:
            return None
        return course.get_marks()
