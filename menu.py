class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_course(self):
        return self.course

    def set_name(self, name):
        self.name = name

    def set_course(self, course):
        self.course = course

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}"


class StudentRecordSystem:
    student_records = {}

    @staticmethod
    def add_student(student_id, name, course):
        if student_id in StudentRecordSystem.student_records:
            print("Student ID already exists!")
        else:
            StudentRecordSystem.student_records[student_id] = Student(student_id, name, course)
            print("Student added successfully.")

    @staticmethod
    def view_student(student_id):
        if student_id in StudentRecordSystem.student_records:
            print(StudentRecordSystem.student_records[student_id])
        else:
            print("Student ID not found.")

    @staticmethod
    def update_student(student_id, name, course):
        if student_id in StudentRecordSystem.student_records:
            student = StudentRecordSystem.student_records[student_id]
            student.set_name(name)
            student.set_course(course)
            print("Student updated successfully.")
        else:
            print("Student ID not found.")

    @staticmethod
    def view_all_students():
        if not StudentRecordSystem.student_records:
            print("No students found.")
        else:
            # Print the table header
            print(f"{'Student ID':<15} {'Name':<20} {'Course':<20}")
            print("-" * 60)

            # Print the student details in a table format
            for student in StudentRecordSystem.student_records.values():
                print(f"{student.get_id():<15} {student.get_name():<20} {student.get_course():<20}")


def main():
    while True:
        print("\nStudent Record System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. View All Students")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            course = input("Enter Student Course: ")
            StudentRecordSystem.add_student(student_id, name, course)

        elif choice == 2:
            student_id = input("Enter Student ID: ")
            StudentRecordSystem.view_student(student_id)

        elif choice == 3:
            student_id = input("Enter Student ID: ")
            name = input("Enter New Student Name: ")
            course = input("Enter New Student Course: ")
            StudentRecordSystem.update_student(student_id, name, course)

        elif choice == 4:
            StudentRecordSystem.view_all_students()

        elif choice == 5:
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
