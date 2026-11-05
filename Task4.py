class BankAccount {
    String accountHolder;
    int accountNumber;
    double balance;

    BankAccount(String name, int number, double bal) {
        accountHolder = name;
        accountNumber = number;
        balance = bal;
    }

    void deposit(double amount) {
        balance = balance + amount;
        System.out.println("Deposited: " + amount);
    }

    void withdraw(double amount) {
        if (balance >= amount) {
            balance = balance - amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient balance");
        }
    }

    void displayDetails() {
        System.out.println("Account Holder: " + accountHolder);
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        BankAccount b = new BankAccount("Ardra", 12345, 5000);

        b.deposit(1000);
        b.withdraw(2000);
        b.displayDetails();
    }
}
