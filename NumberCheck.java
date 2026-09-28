import java.util.Scanner;

public class NumberCheck {

    // Method to check if a number is a Palindrome
    public static boolean isPalindrome(int num) {
        int original = num;
        int reversed = 0;

        while (num > 0) {
            int digit = num % 10;
            reversed = reversed * 10 + digit;
            num /= 10;
        }

        return original == reversed;
    }

    // Method to check if a number is Prime
    public static boolean isPrime(int num) {
        if (num <= 1)
            return false;

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0)
                return false;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number: ");
        int n = sc.nextInt();

        System.out.println(
            n + (isPalindrome(n)
                ? " is a Palindrome."
                : " is NOT a Palindrome.")
        );

        System.out.println(
            n + (isPrime(n)
                ? " is a Prime number."
                : " is NOT a Prime number.")
        );

        sc.close();
    }
}