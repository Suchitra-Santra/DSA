class BankAccount {

    protected String accNumber;
    protected double balance;

    public BankAccount(String accNumber, double balance) {
        this.accNumber = accNumber;
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;

        System.out.println(
            "Deposited $" + amount +
            " | New Balance: $" + balance
        );
    }
}

class SavingsAccount extends BankAccount {

    private double interestRate;

    public SavingsAccount(
        String accNumber,
        double balance,
        double interestRate
    ) {
        super(accNumber, balance);
        this.interestRate = interestRate;
    }

    public void addInterest() {
        double interest = balance * (interestRate / 100);
        deposit(interest);
    }
}

public class BankSystem {

    public static void main(String[] args) {

        SavingsAccount sa =
            new SavingsAccount("SA-1002", 1000.0, 5.0);

        sa.deposit(500.0);
        sa.addInterest();
    }
}