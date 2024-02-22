SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/clock_input.sv

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file

TOPLEVEL = clock_input

#MODULE is the basename of the Python test file

MODULE =clock_1Mhz

include $(shell cocotb-config --makefiles)/Makefile.sim

