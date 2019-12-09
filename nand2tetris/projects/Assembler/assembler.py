from parser import Parser
from translator import Translator
# /home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm

# Opens and cleans the source file. 
# source_file = input('Please enter a valid path to .asm file ')
assembly_program = Parser('/home/uriel/projects-repo/nand2tetris/projects/Assembler/MaxL.asm')

while True:
    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)
    

    if command_type == 'A_COMMAND':
        a_command_bin = assembly_program.symbol_or_decimal(current_command)
        print(a_command_bin)
    elif command_type == 'L_COMMAND':
        pass
    else:   #Else its a C_COMMAND
        dest_mnemonics = assembly_program.dest_mnemonics(current_command)
        comp_mnemonics = assembly_program.comp_mnemonics(current_command)
        jump_mnemonics = assembly_program.jump_mnemonics(current_command)

        # Generate a Translator object, which contains the converted mnemonics to bits
        mnemonics_to_bin = Translator(dest_mnemonics, comp_mnemonics, jump_mnemonics)

        c_command_bin = '111' + mnemonics_to_bin.comp_bits + \
                        mnemonics_to_bin.dest_bits + mnemonics_to_bin.jump_bits

        print(c_command_bin)

    