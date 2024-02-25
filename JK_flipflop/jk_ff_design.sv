/***********************************************************************

Filename:   	jk_ff_design.sv

Author Name:	Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com"

**********************************************************************/
module jk_ff(input clk,rst,j,k,output reg q,q_);

always@(posedge clk) begin
if(rst==1'b1)
begin
q<=1'b0;
q_<=1'b1;
end
else begin
case({j,k})
2'b00:{q,q_}={q,q_};
2'b01:{q,q_}={1'b0,1'b1};
2'b10:{q,q_}={1'b1,1'b0};
2'b11:{q,q_}=~{q,q_};
endcase
end end
initial begin
$dumpfile("waves.vcd");
$dumpvars();
end
endmodule
