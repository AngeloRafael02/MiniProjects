module DLatch(
    input D,enable, //out enable into a clock to make the sircuit into a DFlipFlop
    output wire q1,q2
);
    wire notD,and1,and2;
    not(notD,D);
    and(and1,notD,enable);
    and(and2,D,enable);
    
    assign q1 = ~(and1 | q2);
    assign q2 = ~(and2 | q1);
endmodule

module DLTB;
    reg d,enable;
    wire q1,q2;
    DLatch DL(d,enable,q1,q2);
    initial begin
        enable=0; d=0; 
        $monitor("enable=%b. d=%b, q1=%b, q2=%b",enable,d,q1,q2);
        #5 enable=0; d=1; 
        #5 enable=1; d=0;
        #5 enable=1; d=1;
        #5 $finish;
    end
endmodule
