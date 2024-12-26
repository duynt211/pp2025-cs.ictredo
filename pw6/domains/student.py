class Stdnt:
    def __init__(self, stdnt_id, name, dob):
        self.__stdnt_id = stdnt_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    @property
    def stdnt_id(self):
        return self.__stdnt_id

    @property
    def name(self):
        return self.__name

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
        return f"ID: {self.__stdnt_id}, Name: {self.__name}, DOB: {self.__dob}, GPA: {self.__gpa:.2f}"
