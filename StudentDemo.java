class Student {

    private int id;
    private String name;
    private double marks;

    // Default Constructor
    public Student() {
        this.id = 0;
        this.name = "Unknown";
        this.marks = 0.0;
    }

    // Parameterized Constructor
    public Student(int id, String name, double marks) {
        this.id = id;
        this.name = name;
        this.marks = marks;
    }

    // Method 1
    public void displayInfo() {
        System.out.println(
            "ID: " + id +
            ", Name: " + name +
            ", Marks: " + marks
        );
    }

    // Method Overloading
    public void displayInfo(String remark) {
        System.out.println(
            "ID: " + id +
            ", Name: " + name +
            ", Marks: " + marks +
            " | Remark: " + remark
        );
    }
}

public class StudentDemo {
    public static void main(String[] args) {

        Student s1 = new Student();
        Student s2 = new Student(101, "Rahul Verma", 88.5);

        System.out.println("Student 1 Details:");
        s1.displayInfo();

        System.out.println("\nStudent 2 Details:");
        s2.displayInfo("Passed with Distinction");
    }
}