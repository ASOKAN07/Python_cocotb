'''***********************************************************************

Filename:   	clock_1Mhz.py

Author Name:	Asokan R

Support e-mail: For any queries, reach out to us on "asokanx.dv@gmail.com"

**********************************************************************'''

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer

freq=1e6/1000000
#1e6 is to conevrt this value to us time

@cocotb.test()
async def my_test(dut):
    cocotb.start_soon(Clock(dut.clk,freq,units='us').start())
    await Timer(1,units='ms')

