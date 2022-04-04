// See https://aka.ms/new-console-template for more information
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Calculator{
    public static void Main(){
        while(true){
             Console.WriteLine("Welcome to the Calculator!");
             Console.WriteLine("Enter you first Value/exit: ");
            string strx = Console.ReadLine();
                 if (strx == "exit" || strx == "Exit" || strx == "EXIT"){
                     break;
                 }
                int x = Convert.ToInt32(strx);
            Console.WriteLine("Enter you second Value: ");
                int y = Convert.ToInt32(Console.ReadLine()); 
            Console.WriteLine("Choose your operation: ");
            string ope = Console.ReadLine();
                if (ope == "+") {
                    double answer = x + y;
                    Console.WriteLine("{0} + {1} = {2}",x,y,answer);
                } else if (ope == "-") {
                    double answer = x - y;
                    Console.WriteLine("{0} - {1} = {2}",x,y,answer);
                } else if (ope == "*") {
                    double answer = x * y;
                    Console.WriteLine("{0} * {1} = {2}",x,y,answer);
                 } else if (ope == "/") {
                     double answer = x / y;
                     Console.WriteLine("{0} / {1} = {2}",x,y,answer);
                }
             Console.WriteLine("exit Program? y/n");
            string exit = Console.ReadLine();
            if (exit == "y" || exit == "Y"){
                Console.WriteLine("Thank you for using the Calculator!");
                 break;
             }
        }
    }
}
