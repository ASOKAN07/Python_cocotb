'''***********************************************************************

Filename:   	counter_test.py

Author Name:	Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com"

**********************************************************************'''
import cocotb
from cocotb.triggers import Timer,RisingEdge, FallingEdge 
from cocotb.clock import Clock 
from cocotb.result import TestFailure,TestSuccess,TestError


async def reset(dut):
    await FallingEdge(dut.clk)
    dut.rst.value=1
    dut.load_en.value=0
    dut.upcount_en.value=0
    dut.load_in.value=0
    await FallingEdge(dut.clk)
    dut.rst.value=0
    dut._log.info("Reset done Success")

@cocotb.test()
async def my_test(dut):
    cocotb.start_soon(Clock(dut.clk,1,units='ns').start())
    await reset(dut)
    await Timer(20,units='ns')


    #load_en make it 1 and force load 13
    await FallingEdge(dut.clk)
    dut.load_en.value=1;
    dut.load_in.value=13;
    await FallingEdge(dut.clk)
    dut.load_en.value=0;
    await Timer(20,units='ns')

    #up_counter_en =1 ->it will do downcount
    dut.upcount_en =1;
    await Timer(100,units='ns')
    reset(dut);

