/***********************************************************************

Filename:   	gray_code_converter.sv

Author Name:	Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com"

**********************************************************************/


module gray_code_converter(input [3:0]a,output reg [3:0]gc_output);

always@(*)
begin 
gc_output[3]=a[3];
gc_output[2]=a[3]^a[2];
gc_output[1]=a[2]^a[1];
gc_output[0]=a[1]^a[0];
end

endmodule 
