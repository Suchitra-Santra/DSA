public class MatrixMultiplication {

    public static void main(String[] args) {

        int[][] A = {
            {1, 2, 3},
            {4, 5, 6}
        };

        int[][] B = {
            {7, 8},
            {9, 1},
            {2, 3}
        };

        int r1 = A.length;
        int c1 = A[0].length;

        int r2 = B.length;
        int c2 = B[0].length;

        // Check if multiplication is possible
        if (c1 != r2) {
            System.out.println("Matrix multiplication not possible!");
            return;
        }

        int[][] C = new int[r1][c2];

        // Matrix multiplication
        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c2; j++) {
                for (int k = 0; k < c1; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        // Display result
        System.out.println("Resultant Product Matrix:");

        for (int[] row : C) {
            for (int val : row) {
                System.out.print(val + "\t");
            }
            System.out.println();
        }
    }
}gi