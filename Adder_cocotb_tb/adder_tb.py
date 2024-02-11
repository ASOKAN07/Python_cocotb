'''***********************************************************************  
Filename:        Adder.sv
  
Author Name:    Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com" 	

**********************************************************************'''

import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
no_of_trnx=40

@cocotb.test()
async def addr_test(dut):
    for i in range(no_of_trnx):
        a=cocotb.random.randrange(0,16)
        b=cocotb.random.randrange(0,16)
        carry_in=cocotb.random.randrange(0,1)
        
        #dut Driver 

        dut.a.value=a
        dut.b.value=b
        dut.carry_in.value=carry_in
        await Timer(0,'fs')
        
        #dut._log.info("Input a=%d b=%d carry_in=%d"%(a, b, carry_in))
 
        await Timer(10,"ps")
        sum_=dut.sum.value
        carry_out=dut.carry_out.value
        #dut._log.info("Output sum=%d carry_out=%d"%(sum_,carry_out))
        
        if (a+b+carry_in)>15:
             if(int((bin(a+b+carry_in)[3:]),2)==int((bin(sum_)[2:]),2) and carry_out==1):
                 dut._log.info("Testcase Pass")
             else:
                 dut._log.info("Input a=%d b=%d carry_in=%d"%(a, b, carry_in))
                 dut._log.info("Output sum=%s carry_out=%s"%(bin(sum_),bin(carry_out)))
                 raise TestFailure("Output Sum and Carry is UnExpected")
        else:
             if(bin(a+b+carry_in)[2:]==bin(sum_)[2:] and carry_out==0):
                 dut._log.info("Testcase Pass")
             else:
                 
                 dut._log.info("Input a=%d b=%d carry_in=%d"%(a, b, carry_in))
                 dut._log.info("Output sum=%d carry_out=%d"%(sum_,carry_out))
                 raise TestFailure("Output Sum and Carry is UnExpected")

            

        await Timer(10,"ps")



