class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        for grades in grade:
            if 0<=grades<=100:
                self.grades.append(grades)
            else:
                raise ValueError("Grade must be a number between 0 and 100")

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_details(self):
        return f'Student ID: {self.student_id},Name: {self.name},Grades: {self.grades},Average Grade: {round(self.calculate_average(),2)}'



class School:

    def __init__(self):
        self.students = {}

    def add_student(self, student):
        try:
            if student.student_id in self.students:
                raise ValueError(f"Student with ID {student.student_id} already exists")
            self.students[student.student_id] = student
            print("Student added successfully")
        except ValueError as e:
            print(e)

    def remove_student(self, student_id):
        try:
            if student_id not in self.students:
                raise KeyError(f"Student with ID {student_id} not found")
            del self.students[student_id]
            print("Successfully removed student")
        except KeyError as e:
            print(e)

    def search_student(self, student_id):
        try:
            if student_id not in self.students:
                raise KeyError(f"Student with ID {student_id} not found")
            print("Successfully fetched")
            return self.students[student_id]
        except KeyError as e:
            print(e)

    def __iter__(self):
        for student in self.students.values():
            yield student

class AdvancedSchool(School):
    def find_students_above_threshold(self, threshold):
        try:
            found_student=[student.display_details() for student in self.students.values() if student.calculate_average()>threshold]
            if found_student:
                print("Successfully fetched")
                print("\n".join(found_student))
            else:
                raise ValueError("No student found")
        except ValueError as e:
            print(e)


















