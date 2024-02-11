/***********************************************************************  
Filename:        Adder.sv
  
Author Name:    Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com" 	

************************************************************************/
module adder(a,b,carry_in,sum,carry_out);
input [3:0]a,b;
input carry_in;
output [3:0]sum;
output carry_out;

assign {carry_out,sum}=a+b+carry_in;   

//Waveform Gen
initial begin
$dumpfile("wave.vcd");
$dumpvars();
end 

endmodule
