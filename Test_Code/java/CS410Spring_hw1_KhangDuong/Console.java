package CS410Spring_hw1_KhangDuong;

import java.util.Scanner;

public class Console {
    Scanner sc = new Scanner(System.in);
    public double readNumber(String prompt, double min, double max) {
        double value;
        while (true) {
            System.out.print(prompt);
            value = sc.nextFloat();
            if (value >= min && value <= max)
                break;
            System.out.println("Enter a value between " + min + " and " + max);
        }
        return value;
    }
}
