module halfAdder(A, B, Sum, Carry);
    input A,B;
    output Sum,Carry;

    and(Carry,A,B);
    xor(Sum,A,B);
endmodule

module halfAdderTB;
    reg a,b;
    wire sum,carry;

    halfAdder hfadd(a,b,sum,carry);

    initial
        begin
            a=0; b=0;
            $display("Simulating HalfAdder");
            $monitor("A=%b, B=%b, sum=%b, carry=%b", a,b,sum,carry);
            #10 a=0; b=1;
            #10 a=1; b=0;
            #10 a=1; b=1;
            #10 $finish;
        end
endmodule