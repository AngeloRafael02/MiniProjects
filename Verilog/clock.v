`timescale 1s/1ms

module clockModule();
    reg clk;
    not(not1,clk);
    and(and1,not1,clk);
    or(or1,~clk,clk);
    
    initial
        begin
            $dumpfile("clock.vcd");
	        $dumpvars(-1, clk);
	        $monitor("%b : %b : %b : %b : time = %0t",clk,not1,and1,or1, $realtime);
        end
    initial 
        begin
        clk = 0;
        forever 
            #10 clk = ~clk;
        end
endmodule

//NOTE: > make and and or gate display in gtkwave
//      > find a way to implement clock in other modules/circuits
