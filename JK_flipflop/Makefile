SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/jk_ff_design.sv

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = jk_ff
#MODULE is the basename of the Python test file
MODULE = jk_ff_test
include $(shell cocotb-config --makefiles)/Makefile.sim
