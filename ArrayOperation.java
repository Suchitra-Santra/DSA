import java.util.Scanner;

public class ArrayOperation {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter " + n + " elements:");

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Calculate Sum
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }

        // Calculate Average
        double avg = (double) sum / n;

        System.out.println("Sum of elements: " + sum);
        System.out.println("Average of elements: " + avg);

        // Linear Search
        System.out.print("Enter element to search: ");
        int target = sc.nextInt();

        boolean found = false;

        for (int i = 0; i < n; i++) {
            if (arr[i] == target) {
                System.out.println("Element " + target +
                        " found at index position " + i);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("Element " + target +
                    " not found in the array.");
        }

        sc.close();
    }
}