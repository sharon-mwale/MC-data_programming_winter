if __name__ == "__main__":
    class Student:
        def __init__(self, name, age, grade):
            self.name = name
            self.grade = grade

        def get_name(self):
            return self.name

        def get_grade(self):
            return self.grade

    # Create a list of Student objects
    students = [
        Student("Alice", 18, "A"),
        Student("Charlie", 19, "A"),
    ]

    # Use list comprehension to filter students with grade 'A'
    grade_a_students = [student for student in students if student.get_grade() == 'A']

    # Print the names of students with grade 'A'
    print("Students with grade 'A':")
    for student in grade_a_students:
        print(student.get_name())

