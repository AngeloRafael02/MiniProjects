/*Simple Arithmetic Calculator
 * By: Angelo Rafael F. Recio
 * 2020251-BISCPE
 */
import java.awt.event.ActionListener;
import java.awt.Color;
import java.awt.event.*;
import javax.swing.*;

public class JavaSwingCalculator{
    public static JFrame mainF;
    public static void app() throws NumberFormatException{
               mainF = new JFrame("Calculator");
               mainF.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
               mainF.getContentPane().setBackground(Color.lightGray);
               mainF.setResizable(false);
        JLabel title = new JLabel("Simple Arithmetic Calculator by: Angelo Rafael Recio");
               title.setBounds(50, 10, 500, 30);
        JLabel label1 = new JLabel("Input First Number.");
               label1.setBounds(50, 50, 200, 30); 
        JTextField input1 = new JTextField();
                  input1.setBounds(50, 75, 200, 20); 
                  input1.addKeyListener(new KeyAdapter(){
                    public void keyPressed(KeyEvent ke){
                        inputValidate(ke, input1);
                    }   
                  });
        JLabel label2 = new JLabel("Input Second Number.");
               label2.setBounds(50,100, 200,30);
        JTextField input2 = new JTextField();
                  input2.setBounds(50,125, 200, 20); 
                  input2.addKeyListener(new KeyAdapter(){
                    public void keyPressed(KeyEvent ke){
                        inputValidate(ke, input2);
                    }
                  });
        JLabel label3 = new JLabel("Input Operation.");
               label3.setBounds(50,150, 200,30); 
        String[] operations = {"Addition","Subtraction","Multiplication","Division"};
        JComboBox<String> input3 = new JComboBox<String>(operations);
                  input3.setBounds(50,175, 200,30);
        JLabel results = new JLabel("Answer here...");
               results.setBounds(300,125, 100, 20);
        JButton execute = new JButton("Calculate");
                execute.setBounds(300, 50, 100, 30);
                execute.addActionListener(new ActionListener(){
                    public void actionPerformed(ActionEvent e) throws NumberFormatException{
                        try {
                            results.setText(Float.toString(
                                calculate(Float.parseFloat(input1.getText()),
                                          Float.parseFloat(input2.getText()),
                                          (String) input3.getSelectedItem())
                            ));                              
                        } catch (Exception err) {           
                            System.out.println(err);
                            JOptionPane.showMessageDialog(mainF,"Wrong/Empty Input","Error",JOptionPane.ERROR_MESSAGE);
                            throw new NumberFormatException("Wrong/Empty Input");
                        }
                    }
                });

        mainF.add(title); mainF.add(label1); mainF.add(label2); mainF.add(input1); mainF.add(input2);
        mainF.add(label3); mainF.add(input3); mainF.add(execute); mainF.add(results);
        
        mainF.setSize(500,300);
        mainF.setLayout(null);  
        mainF.setVisible(true); 
    }
    public static void inputValidate(KeyEvent ke,JTextField InputComponent){
        String field = InputComponent.getText();
        if ((ke.getKeyChar() >= '0' && ke.getKeyChar() <= '9' )
            ||(ke.getKeyChar() == '.' && field.chars().filter(ch -> ch == '.').count() <= 0)
            || ke.getKeyCode() == KeyEvent.VK_BACK_SPACE
            ){
            InputComponent.setEditable(true);
        } else{
            InputComponent.setEditable(false);
        }
    }
    public static float calculate(float num1, float num2, String operation) throws ArithmeticException {
        switch (operation) {
            case "Addition":  
                return num1 + num2;
            case "Subtraction":  
                return num1 - num2;
            case "Multiplication":  
                return num1 * num2;
            case "Division":  
                if (num2 == 0){
                    JOptionPane.showMessageDialog(mainF,"Cannot divide by Zero","Error",JOptionPane.ERROR_MESSAGE);
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
        app();
    }
}