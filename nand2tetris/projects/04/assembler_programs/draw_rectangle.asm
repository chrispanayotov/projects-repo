// Create a n x m rectangle by manipulating the screen register
// PSEUDO CODE:
// addr = SCREEN
// n = RAM[0]
// i = 0
// LOOP:
//  if i > n goto END
//  RAM[addr] = -1 (set pixels to black)
//  addr = addr + 31
//  i = i + 1
//  goto LOOP
// END:
//  goto END

  @SCREEN
  D=A
  @addr
  M=D   // addr = 16384 register

  @R0
  D=M
  @n
  M=D   // n = RAM[0]

  @i
  M=0
  
(LOOP)
  @i
  D=M
  @n
  D=D-M
  @END
  D;JGT   // if i > n goto END

  @addr
  A=M
  M=-1    // sets RAM[addr] = 1111111111111111

  @i
  M=M+1   // i = i + 1
  @32
  D=A
  @addr
  M=D+M   // addr = addr + 32
  
  @LOOP
  0;JMP

(END)
  @END
  0;JMP