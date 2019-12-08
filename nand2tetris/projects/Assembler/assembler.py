from parser import Parser

# new_file = Parser('/home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm')

assembly_program = Parser('/home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm')

while True:

    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)
    

    if command_type == 'A':
        a_command_bin = assembly_program.symbol_or_decimal(current_command)
        print(a_command_bin)
    elif command_type == 'L':
        pass
    else:   # Command is C
        pass