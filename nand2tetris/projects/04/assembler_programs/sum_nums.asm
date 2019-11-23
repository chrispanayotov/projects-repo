// Create a program that sums numbers from 1 to n
// Store them in R1

  @R0
  D=M
  @n  // n = R0
  M=D
  @i
  M=1  // i = 1
  @sum
  M=0

(LOOP)
  @i
  D=M
  @n
  D=D-M
  @STOP
  D;JGT   // if i > n goto STOP

  @sum
  D=M
  @i
  D=D+M
  @sum    // sum = sum + i
  M=D
  @i
  M=M+1   // i = i + 1
  @LOOP
  0;JMP

(STOP)
  @sum
  D=M
  @R1
  M=D   // R1 = sum

(END)
  @END
  0;JMP