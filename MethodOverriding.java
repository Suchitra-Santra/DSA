class Payment {

    public void processPayment() {
        System.out.println("Processing generic payment...");
    }
}

class CreditCardPayment extends Payment {

    @Override
    public void processPayment() {
        System.out.println(
            "Processing Credit Card Payment... Validating card details."
        );
    }
}

class PayPalPayment extends Payment {

    @Override
    public void processPayment() {
        System.out.println(
            "Processing PayPal Payment... Connecting to API."
        );
    }
}

public class MethodOverriding {

    public static void main(String[] args) {

        Payment pay1 = new CreditCardPayment();
        Payment pay2 = new PayPalPayment();

        pay1.processPayment();
        pay2.processPayment();
    }
}