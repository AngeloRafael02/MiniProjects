module SRLatch(
    input wire s,r,
    output wire q1,q2);

    assign q1 = ~(r & q2);
    assign q2 = ~(s & q1);
endmodule

module SRLTB;
    reg s,r;
    wire q1,q2;

    SRLatch SRL(s,r,q1,q2);
    initial begin
        #1 s=0;r=0;
        #1 $display("HalfAdder");
           $monitor($time,,,"s=%b, r=%b, q1=%b, q2=%b",s,r,q1,q2);
        #1 s=0;r=1;
        #1 s=1;r=0;
        #1 s=1;r=1;
        #1 $finish;
    end
endmodule