package CS410Spring_hw1_KhangDuong;

public class CS410Spring_hw1_KhangDuong {
    public static void main(String[] args) {
        Console console = new Console();

        int principal = (int) console.readNumber("Principal: ", 1000, 1_000_000);
        float annualInterest = (float) console.readNumber("Annual Interest Rate: ", 1, 30);
        byte years = (byte) console.readNumber("Period (Years): ", 1, 30);

        Mortgage_Report obj = new Mortgage_Report(principal, annualInterest, years);
        obj.printMortgage();
        obj.printPaymentSchedule();
    }
}
