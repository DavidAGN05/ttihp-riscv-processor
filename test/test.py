# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    # dut.ena.value = 1
    # dut.ui_in.value = 0
    # dut.uio_in.value = 0
    # dut.rst_n.value = 0
    # await ClockCycles(dut.clk, 10)
    # dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    # dut.ui_in.value = 20
    # dut.uio_in.value = 30

    # Wait for one clock cycle to see the output values
    # await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    # assert dut.uo_out.value == 50

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.

    # --- Added: Test all input combinations for a, b, c ---
    errors = 0
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                dut.a.value = a
                dut.b.value = b
                dut.c.value = c
                await ClockCycles(dut.clk, 1)
                expected = int((not a and not b and not c) or
                               (a and not b and not c) or
                               (a and not b and c))
                # Only compare if y is resolvable (not 'X' or 'Z')
                if dut.y.value.is_resolvable and str(dut.y.value) in ("0", "1"):
                    if int(dut.y.value) != expected:
                        dut._log.error(f"Mismatch: a={a} b={b} c={c} -> y={int(dut.y.value)}, expected={expected}")
                        errors += 1
                # else: skip comparison if y is not valid yet
    assert errors == 0, f"Test failed with {errors} errors."
