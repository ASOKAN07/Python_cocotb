SIM ?= icarus

TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/gray_code_converter.sv

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file

TOPLEVEL = gray_code_converter

#MODULE is the basename of the Python test file

MODULE =gray_code_test

include $(shell cocotb-config --makefiles)/Makefile.sim
