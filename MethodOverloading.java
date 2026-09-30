class Calculator {

    // Add two integers
    public int add(int a, int b) {
        return a + b;
    }

    // Add three integers
    public int add(int a, int b, int c) {
        return a + b + c;
    }

    // Add two double values
    public double add(double a, double b) {
        return a + b;
    }
}

public class MethodOverloading {

    public static void main(String[] args) {

        Calculator calc = new Calculator();

        System.out.println("Sum of 2 ints: " + calc.add(10, 20));

        System.out.println("Sum of 3 ints: " + calc.add(10, 20, 30));

        System.out.println("Sum of 2 doubles: " + calc.add(5.5, 4.5));
    }
}