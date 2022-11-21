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
        s=0;r=0;
        $monitor("s=%b, r=%b, q1=%b, q2=%b",s,r,q1,q2);
        #5 s=0;r=1;
        #5 s=1;r=0;
        #5 s=1;r=1;
        #5 $finish;
    end
endmodule