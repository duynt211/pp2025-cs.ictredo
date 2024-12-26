def show_students(students):
    print("Registered Students:")
    for student in students:
        print(student)


def show_courses(courses):
    print("Available Courses:")
    for course in courses:
        print(course)


def show_marks(course, students):
    print(f"Marks for {course.title}:")
    for stdnt_id, mark in course.get_marks().items():
        student = next((s for s in students if s.stdnt_id == stdnt_id), None)
        if student:
            print(f"{student.name}: {mark}")


def show_gpa(students):
    print("GPA of Students:")
    for student in students:
        print(f"{student.name}: GPA = {student.gpa:.2f}")
