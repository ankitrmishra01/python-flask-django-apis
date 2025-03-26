#A program that simulates a school management system, with classes for the students, the teachers, and the courses.

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []  # List to hold enrolled courses

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} enrolled in {course.course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course.course_name}.")

    def view_courses(self):
        if self.courses:
            print(f"{self.name}'s Courses:")
            for course in self.courses:
                print(f"- {course.course_name}")
        else:
            print(f"{self.name} is not enrolled in any courses.")

class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.courses = []  # List to hold courses the teacher teaches

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} is now teaching {course.course_name}.")
        else:
            print(f"{self.name} is already teaching {course.course_name}.")

    def view_courses(self):
        if self.courses:
            print(f"{self.name}'s Courses:")
            for course in self.courses:
                print(f"- {course.course_name}")
        else:
            print(f"{self.name} is not teaching any courses.")

class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = []  # List to hold enrolled students
        self.teacher = None  # The teacher assigned to the course

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} has been added to {self.course_name}.")
        else:
            print(f"{student.name} is already enrolled in {self.course_name}.")

    def assign_teacher(self, teacher):
        if self.teacher is None:
            self.teacher = teacher
            teacher.assign_course(self)  # Automatically assigns course to teacher
            print(f"{teacher.name} is now the teacher for {self.course_name}.")
        else:
            print(f"{self.course_name} already has a teacher: {self.teacher.name}.")

    def view_students(self):
        if self.students:
            print(f"Students enrolled in {self.course_name}:")
            for student in self.students:
                print(f"- {student.name}")
        else:
            print(f"No students enrolled in {self.course_name}.")


# Create some students
student1 = Student(student_id="S001", name="Alice")
student2 = Student(student_id="S002", name="Bob")
student3 = Student(student_id="S003", name="Charlie")

# Create some teachers
teacher1 = Teacher(teacher_id="T001", name="Mr. Smith")
teacher2 = Teacher(teacher_id="T002", name="Ms. Johnson")

# Create some courses
course1 = Course(course_code="CS101", course_name="Computer Science 101")
course2 = Course(course_code="MATH101", course_name="Mathematics 101")

# Assign teachers to courses
course1.assign_teacher(teacher1)
course2.assign_teacher(teacher2)

# Enroll students in courses
student1.enroll(course1)
student1.enroll(course2)

student2.enroll(course1)

# View student courses
student1.view_courses()
student2.view_courses()

# View teacher's courses
teacher1.view_courses()
teacher2.view_courses()

# View enrolled students for each course
course1.view_students()
course2.view_students()
