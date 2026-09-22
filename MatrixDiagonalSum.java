import java.util.Scanner;

public class MatrixDiagonalSum {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter matrix order (N x N): ");
        int n = sc.nextInt();

        int[][] matrix = new int[n][n];

        System.out.println("Enter elements of matrix:");

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        System.out.println("Entered Matrix:");

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }

        // Main Diagonal Sum
        int diagonalSum = 0;

        for (int i = 0; i < n; i++) {
            diagonalSum += matrix[i][i];
        }

        System.out.println(
            "Sum of Main Diagonal Elements: " + diagonalSum
        );

        sc.close();
    }
}