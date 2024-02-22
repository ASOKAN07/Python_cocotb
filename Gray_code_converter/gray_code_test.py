'''***********************************************************************

Filename:   	gray_code_test.py

Author Name:	Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com"

**********************************************************************'''


import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
no_trnx=20;

@cocotb.test()
async def my_test(dut):
    for i in range(no_trnx):
        dut.a.value=cocotb.random.randrange(0,16)

        await Timer(1,'ns')
        print("Transmitted data a= ",dut.a.value)

        #monitor the output and compare
        print("Gray code output =",dut.gc_output.value)
        if((dut.a.value)^(dut.a.value>>1)==dut.gc_output.value):
            dut.log.info("Test Case Pass")
        else:
            raise cocotb.result.TestFailure("Convertion get failed**")
            await Timer(1,'ns')



