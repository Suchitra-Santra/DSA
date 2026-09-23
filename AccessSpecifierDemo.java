class BankAccount {

    // Private variables
    private String accountNumber;
    private double balance;

    public BankAccount(String accountNumber, double initialBalance) {
        this.accountNumber = accountNumber;

        if (initialBalance >= 0) {
            this.balance = initialBalance;
        } else {
            this.balance = 0;
        }
    }

    // Getter
    public String getAccountNumber() {
        return accountNumber;
    }

    // Getter
    public double getBalance() {
        return balance;
    }

    // Deposit
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println(
                "Successfully deposited: $" + amount
            );
        } else {
            System.out.println("Invalid deposit amount.");
        }
    }

    // Withdraw
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println(
                "Successfully withdrew: $" + amount
            );
        } else {
            System.out.println(
                "Insufficient funds or invalid withdrawal amount."
            );
        }
    }
}

public class AccessSpecifierDemo {
    public static void main(String[] args) {

        BankAccount acc =
            new BankAccount("ACC-98765", 5000.0);

        System.out.println(
            "Account Number: " + acc.getAccountNumber()
        );

        System.out.println(
            "Initial Balance: $" + acc.getBalance()
        );

        acc.deposit(1500.0);
        acc.withdraw(2000.0);

        System.out.println(
            "Final Balance: $" + acc.getBalance()
        );
    }
}