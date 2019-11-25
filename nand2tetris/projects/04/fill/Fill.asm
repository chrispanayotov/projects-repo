// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
// Range of SCREEN Registers is 16384 - 24575

(RESTART)
  @SCREEN   // Select SCREEN register
  D=A
  @R0    // Put it at location 0 
  M=D

(KBDINPUT)    // Create an infinite loop that listens to the keyboard input
  @KBD
  D=M
  @DARKEN   // If a key is pressed it means that KBD register is not 0 (JGT)
  D;JGT     // -> jump to DARKEN block
  @WHITEN   // If a key is not pressed it means that KBD register is 0 (JEQ)
  D;JEQ     // -> jump to WHITEN block

  @KBDINPUT   // LOOP
  0;JMP

(DARKEN)
  @R1
  M=-1    // If a key is pressed DARKEN the screen
  @CHANGE
  0;JMP

(WHITEN)
  @R1
  M=0     // If no key is pressed don't fill in the screen
  @CHANGE
  0;JMP

(CHANGE)
  @R1     // Checks whether to darken or whiten the screen
  D=M

  @R0
  A=M     // Gets the address of which pixel to fill and then fills it 
  M=D

  @R0     // Switch to next pixel
  D=M+1
  @KBD
  D=A-D

  @R0
  M=M+1   // Switch to next pixel
  A=M

  @CHANGE
  D;JGT

  @RESTART
  0;JMP