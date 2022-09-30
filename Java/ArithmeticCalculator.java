import java.util.Scanner;

public class ArithmeticCalculator {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("Input First Number: ");
        float Input1 = input.nextFloat();
        System.out.print("Input Second Number: ");
        float Input2 = input.nextFloat();

        System.out.println("Input Operation: ");
        char operation = input.next().charAt(0);
        if(operation == '+'){
            System.out.println(Input1 + Input2);
        } else if(operation == '-'){
            System.out.println(Input1 - Input2);
        } else if(operation == '*'){
            System.out.println(Input1 - Input2);
        } else if(operation == '/'){
            System.out.println(Input1 - Input2);
        }else {
            System.out.println("???");
        }
 
        input.close();
    }
}
