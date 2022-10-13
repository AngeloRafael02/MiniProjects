import java.util.Scanner;

public class ArithmeticCalculator {
    public static float calculate(float num1, float num2, char operation) 
    throws ArithmeticException {
        switch (operation) {
            case '+':  
                return num1 + num2;
            case '-':  
                return num1 - num2;
            case '*':  
                return num1 * num2;
            case '/':  
                if (num2 == 0){
                    throw new ArithmeticException("Cannot divide by Zero");
                } else {
                    return num1 / num2;}
            default:
                System.out.println("Error: Incorrect operation input");
                break;
        }
        return 0;
    } 
    public static void main(String[] args){
        try {
            Scanner input = new Scanner(System.in);
            System.out.print("Input First Number: ");
            float Input1 = input.nextFloat();
            System.out.print("Input Second Number: ");
            float Input2 = input.nextFloat();
            System.out.println("Input Operation: ");
            char operation = input.next().charAt(0);
            input.close();
            float answer = calculate(Input1, Input2, operation);
            System.out.println("Answer: " + answer);
        } catch (Exception e) {
            System.out.print(e);
        } finally {
            System.out.println("Program has Ended");
        }
        
    }
}
