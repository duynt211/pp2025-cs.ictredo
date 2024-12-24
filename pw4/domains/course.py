import math

class Crs:
    def __init__(self, crs_id, title, credits):
        self.__crs_id = crs_id
        self.__title = title
        self.__credits = credits
        self.__marks = {}

    @property
    def crs_id(self):
        return self.__crs_id

    @property
    def title(self):
        return self.__title

    @property
    def credits(self):
        return self.__credits

    def add_mark(self, stdnt_id, mark):
        mark = math.floor(mark * 10) / 10.0
        if 0 <= mark <= 20:
            self.__marks[stdnt_id] = mark
        else:
            raise ValueError("Mark must be between 0 and 20.")

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f"Course ID: {self.__crs_id}, Title: {self.__title}, Credits: {self.__credits}"
