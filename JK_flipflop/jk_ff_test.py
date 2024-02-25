'''***********************************************************************

Filename:   	jk_ff_test.py

Author Name:	Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com"

**********************************************************************'''
import cocotb
from cocotb.triggers import Timer,RisingEdge,FallingEdge
from cocotb.clock import Clock
from cocotb.result import TestFailure, TestSuccess

async def reset(dut):
	await FallingEdge(dut.clk)
	dut.rst.value=1
	await FallingEdge(dut.clk)
	dut.rst.value=0
	dut.j.value=0
	dut.k.value=0
	dut._log.info("Reset applied Succesfuly")

@cocotb.test()
async def my_test(dut):
    cocotb.start_soon(Clock(dut.clk,1,units='ns').start())
    await reset(dut)
    for i in range(20):
        q_prev=dut.q.value
        q__prev=dut.q_.value
        await FallingEdge(dut.clk)
        dut.j.value=cocotb.random.randrange(0,2)
        dut.k.value=cocotb.random.randrange(0,2)

        await RisingEdge(dut.clk)
        await Timer(100,units='ps')#Hold time
        if(dut.j.value==0 and dut.k.value==0):
            if(dut.q.value==q_prev and dut.q_.value==q__prev):
                dut._log.info("Test Case is get passed")
            else:
                raise TestFailure("TesteCase get failed**")
        elif(dut.j.value==0 and dut.k.value==1):
            if(dut.q.value==0 and dut.q_.value==1):
                dut._log.info("Test Case is get passed")
            else:
                raise TestFailure("TesteCase get failed**")
        elif(dut.j.value==1 and dut.k.value==0):
            if(dut.q.value==1 and dut.q_.value==0):
                dut._log.info("Test Case is get passed")
            else:
                raise TestFailure("TesteCase get failed**")
        elif(dut.j.value==1 and dut.k.value==1):
            if(dut.q.value!=q_prev and dut.q_.value!=q__prev):
                dut._log.info("Test Case is get passed")
            else:
                raise TestFailure("TesteCase get failed**")
        else:
            raise TestFailure("TesteCase in not valid x or z failed**")

    raise TestSuccess("Every teste case Get passed")

