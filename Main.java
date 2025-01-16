import java.util.HashMap;
import java.util.Scanner;

class Student {
    private String id;
    private String name;
    private String course;

    public Student(String id, String name, String course) {
        this.id = id;
        this.name = name;
        this.course = course;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getCourse() {
        return course;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setCourse(String course) {
        this.course = course;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", Name: " + name + ", Course: " + course;
    }
}

public class Main {
    private static HashMap<String, Student> studentRecords = new HashMap<>();

    public static void addStudent(String id, String name, String course) {
        if (studentRecords.containsKey(id)) {
            System.out.println("Student ID already exists!");
        } else {
            studentRecords.put(id, new Student(id, name, course));
            System.out.println("Student added successfully.");
        }
    }

    public static void viewStudent(String id) {
        if (studentRecords.containsKey(id)) {
            System.out.println(studentRecords.get(id));
        } else {
            System.out.println("Student ID not found.");
        }
    }

    public static void updateStudent(String id, String name, String course) {
        if (studentRecords.containsKey(id)) {
            Student student = studentRecords.get(id);
            student.setName(name);
            student.setCourse(course);
            System.out.println("Student updated successfully.");
        } else {
            System.out.println("Student ID not found.");
        }
    }

  public static void viewAllStudents() {
    if (studentRecords.isEmpty()) {
        System.out.println("No students found.");
    } else {
        // Print the table header
        System.out.println(String.format("%-15s %-20s %-20s", "Student ID", "Name", "Course"));
        System.out.println("-------------------------------------------------------------");

        // Print the student details in a table format
        for (Student student : studentRecords.values()) {
            System.out.println(String.format("%-15s %-20s %-20s", student.getId(), student.getName(), student.getCourse()));
        }
    }
}


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        
        do {
            System.out.println("\nStudent Record System");
            System.out.println("1. Add Student");
            System.out.println("2. View Student");
            System.out.println("3. Update Student");
            System.out.println("4. View All Students");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter Student ID: ");
                    String addId = scanner.nextLine();
                    System.out.print("Enter Student Name: ");
                    String addName = scanner.nextLine();
                    System.out.print("Enter Student Course: ");
                    String addCourse = scanner.nextLine();
                    addStudent(addId, addName, addCourse);
                    break;

                case 2:
                    System.out.print("Enter Student ID: ");
                    String viewId = scanner.nextLine();
                    viewStudent(viewId);
                    break;

                case 3:
                    System.out.print("Enter Student ID: ");
                    String updateId = scanner.nextLine();
                    System.out.print("Enter New Student Name: ");
                    String updateName = scanner.nextLine();
                    System.out.print("Enter New Student Course: ");
                    String updateCourse = scanner.nextLine();
                    updateStudent(updateId, updateName, updateCourse);
                    break;

                case 4:
                    viewAllStudents();
                    break;

                case 5:
                    System.out.println("Exiting system...");
                    break;

                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        } while (choice != 5);

        scanner.close();
    }
}
