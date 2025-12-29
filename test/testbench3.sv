// 4.39: testbench example 3

module testbench3();
  logic        clk, reset;
  logic        a, b, c, y;

  // VCD waveform dump for GTKWave
  initial begin
    $dumpfile("testbench3.vcd");
    $dumpvars(0, testbench3);
  end

  // instantiate device under test
  sillyfunction dut(a, b, c, y);

  // generate clock
  always 
    begin
      clk = 1; #5; clk = 0; #5;
    end

  // All test logic is now handled by cocotb (Python). No SV test vectors or checking.
endmodule
