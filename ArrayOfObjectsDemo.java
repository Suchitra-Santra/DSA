import java.util.Scanner;

class Employee {

    private int empId;
    private String name;
    private double salary;

    public Employee(int empId, String name, double salary) {
        this.empId = empId;
        this.name = name;
        this.salary = salary;
    }

    public void displayRecord() {
        System.out.println(
            "ID: " + empId +
            " Name: " + name +
            " Salary: $" + salary
        );
    }
}

public class ArrayOfObjectsDemo {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter total number of employees: ");
        int count = sc.nextInt();

        Employee[] employees = new Employee[count];

        for (int i = 0; i < count; i++) {

            System.out.println(
                "\nEnter details for Employee " + (i + 1) + ":"
            );

            System.out.print("ID: ");
            int id = sc.nextInt();

            sc.nextLine();

            System.out.print("Name: ");
            String name = sc.nextLine();

            System.out.print("Salary: ");
            double salary = sc.nextDouble();

            employees[i] =
                new Employee(id, name, salary);
        }

        System.out.println("\n--- EMPLOYEE RECORDS ---");

        for (int i = 0; i < count; i++) {
            employees[i].displayRecord();
        }

        sc.close();
    }
}