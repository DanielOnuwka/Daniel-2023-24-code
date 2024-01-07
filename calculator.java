import java.until.Scanner;
// Tells java that we want to use the scanner

public class App {

    public static void main(String [] args) {
        Scanner keyboardInput = new Scanner(System.in;)
        System.out.print("Enter in first Number: ");
        double num1 = keyboardInput.nextDouble();
        System.out.print("Enter in second Number: ");
        double num2 = keyboardInput.nextDouble();
        //Tells java that we want to take what the user input and create a double variable
       System.out.printIn(num1 + num2);
       
    }

}
