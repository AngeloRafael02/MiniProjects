module fullSubtract(A,B,D,bIn,bOut);
    input A,B,bIn;
    output D,bOut;
    wire not1,xor1,and1,not2,and2;

    not(not1,A);
    xor(xor1,A,B);
    and(and1,not1,B);
    not(not2,xor1);
    xor(D,xor1,bIn);
    and(and2,not2,bIn);
    or(bOut,and2,and1);
endmodule

module fullSubtractTB;
    reg A,B,bIn;
    wire D,bOut;

    fullSubtract fstb(A,B,D,bIn,bOut);
    
    initial
        begin
            $dumpfile("fullSubtract.vcd");
	        $dumpvars(-1, fstb);
	        $monitor("%b", A);
        end

    initial
        begin
            A=1'b0; B=1'b0; bIn=1'b0;
            $monitor($time,,,"A=%b, B=%b, bIn=%b, D=%b, bOut=$b", A,B,bIn,D,bOut);
            #2 A=1'b0; B=1'b0; bIn=1'b1;
            #2 A=1'b0; B=1'b1; bIn=1'b0;
            #2 A=1'b0; B=1'b1; bIn=1'b1;
            #2 A=1'b1; B=1'b0; bIn=1'b0;
            #2 A=1'b1; B=1'b0; bIn=1'b1;
            #2 A=1'b1; B=1'b1; bIn=1'b0;
            #2 A=1'b1; B=1'b1; bIn=1'b1;
            #2 $finish;            
        end
endmodule