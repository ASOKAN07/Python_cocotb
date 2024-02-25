SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/counter.sv

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = counter
#MODULE is the basename of the Python test file
MODULE = counter_test
include $(shell cocotb-config --makefiles)/Makefile.sim
