module halfSubtract(A,B,D,bOut);
    input A,B;
    output D,bOut;
    wire not1;

    xor(D,A,B);
    not(not1,A);
    and(bOut,B,not1);
endmodule

module halfSubtractTB;
    reg a,b;
    wire d,bOut;

    halfSubtract hfsbt(a,b,d,bOut);

    initial
        begin
            $dumpfile("halfSubtract.vcd");
	        $dumpvars(-1, hfsbt);
	        $monitor("%b", d,bOut);
        end

    initial 
        begin
            a=0; b=0; 
            
            $display("Simulating Full Adder");
            $monitor("A=%b, B=%b, D=%b, bOut=%b",a,b,d,bOut);

            #10 a=0; b=1; 
            #10 a=1; b=0; 
            #10 a=1; b=1; 
            #10 $finish;
        end
endmodule