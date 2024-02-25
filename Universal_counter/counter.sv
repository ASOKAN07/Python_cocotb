/***********************************************************************

Filename:   	counter.sv

Author Name:	Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com"

**********************************************************************/


module counter(input clk,load_en,rst,upcount_en,input [3:0] load_in,output reg [3:0]counter_out);

always@(posedge clk) begin 
if(rst==1'b1)
	counter_out=4'd0;
else

begin 
if(load_en)
	counter_out=load_in;
else begin 
if(!upcount_en)
	counter_out=counter_out+1;
else
	counter_out=counter_out-1;
end end end

initial begin
$dumpfile("waves.vcd");
$dumpvars();
end
endmodule 
