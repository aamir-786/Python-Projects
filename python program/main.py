# Import the student module
import student_module as sm

# Menu-driven interface
def menu():
    while True:
        print("\nStudent Registration System")
        print("1. Add Student")
        print("2. View Student by ID")
        print("3. Delete Student")
        print("4. Save to File")
        print("5. Load from File")
        print("6. View All Students")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            major = input("Enter Major: ")
            sm.add_student(student_id, name, age, major)
        
        elif choice == "2":
            student_id = input("Enter Student ID: ")
            student = sm.get_student(student_id)
            if student:
                print(f"Student Details: {student}")
        
        elif choice == "3":
            student_id = input("Enter Student ID: ")
            sm.delete_student(student_id)
        
        elif choice == "4":
            sm.save_to_file()
        
        elif choice == "5":
            sm.load_from_file()
        
        elif choice == "6":
            sm.view_all_students()
        
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
