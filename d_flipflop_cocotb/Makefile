SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/dff_design.sv

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = d_ff
#MODULE is the basename of the Python test file
MODULE = dff_test
include $(shell cocotb-config --makefiles)/Makefile.sim
