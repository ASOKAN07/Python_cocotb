/***********************************************************************

Filename:   	dff_design.sv

Author Name:	Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com"

**********************************************************************/

module d_ff(input clk,rst,d,output reg q,q_);

always@(posedge clk) begin
if(rst==1'b1)
begin
q<=1'b0;
q_<=1'b1;
end

else begin
q<=d;
q_<=~d;
end
end

initial begin
$dumpfile("waves.vcd");
$dumpvars();
end

endmodule
