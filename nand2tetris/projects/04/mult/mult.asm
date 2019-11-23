// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Pseudo code:
//  n1 = input()
//  n2 = input()
//  counter = 0
// LOOP:
//  if counter >= n2 goto STOP
//  n1 += n1
//  goto LOOP
// STOP:
//  R2 = n1
// END

// Set variables
  @R0
  D=M
  @END
  D;JEQ

  @n1   // First digit provided by user
  M=D

  @R1
  D=M
  @END
  D;JEQ

  @n2   // Second digit provided by user
  M=D

  @counter  // counter = 0
  M=0
  @sum  // sum = 0
  M=0

(LOOP)
  @counter
  D=M
  @counter
  D=D+1
  @counter  // Loop while counter is less than n2
  M=D
  @n2
  D=D-M
  @STOP   // If counter >= goto STOP
  D;JGT

  @n1 
  D=M
  @sum
  D=D+M   // n1 += n1
  @sum
  M=D

  @LOOP   // goto LOOP
  D;JGT

(STOP)
  @sum
  D=M
  @R2   // Save the result to R2
  M=D

(END)
  @END
  0;JMP