'''***********************************************************************

Filename:   	dff_test.py

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
    dut._log.info("Reset applied Succesfuly")
@cocotb.test()
async def my_test(dut):
    cocotb.start_soon(Clock(dut.clk,1,units='ns').start())
    await reset(dut)
    for i in range(20):
        await FallingEdge(dut.clk)
        dut.d.value=cocotb.random.randrange(0,2)
        await FallingEdge(dut.clk)
        if(dut.q.value==dut.d.value and dut.q_.value!=dut.d.value): 
            dut._log.info("Test Case is get passed")
        else:
            raise TestFailure("TesteCase get failed**")

    raise TestSuccess("Every teste case Get passed")
