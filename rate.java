import java.util.Scanner;

public class RateConstantCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get user input
        System.out.print("Enter the reaction rate (Rate): ");
        double rate = scanner.nextDouble();

        System.out.print("Enter the concentration of A [A]: ");
        double concentrationA = scanner.nextDouble();

        System.out.print("Enter the order of reaction with respect to A (m): ");
        int orderA = scanner.nextInt();

        System.out.print("Enter the concentration of B [B]: ");
        double concentrationB = scanner.nextDouble();

        System.out.print("Enter the order of reaction with respect to B (n): ");
        int orderB = scanner.nextInt();

        // Calculate rate constant
        double k = rate / (Math.pow(concentrationA, orderA) * Math.pow(concentrationB, orderB));

        // Display result
        System.out.printf("The rate constant (k) is: %.5f%n", k);

        scanner.close();
    }
}
