from parser import Parser
from symbol_table import SymbolTable
from translator import Translator, convert_to_bin

# /home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm

# Opens and cleans the source file. 
# source_file = input('Please enter a valid path to .asm file ')
assembly_program = Parser('/home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm')

# Create the SymbolTable and add the built-ins
symbol_table = SymbolTable()


# Do a first run of the assembly program.
# Goal is to scan the progam for LABELS and them to symbol table
while not assembly_program.is_parsed():
    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)
    
    if command_type == 'L_COMMAND':
        label = current_command[1:len(current_command)-1]

        if not symbol_table.contains(label):
            # Adds label and corresponding address (line number) to symbol table 
            symbol_table.add_entry(label, assembly_program.line_counter)

# After the first run is complete removes all (XXX) labels from assembly program 
# and start from the beginning of program:
assembly_program.remove_labels()
assembly_program.line_counter = 0


# Do a second run of the assembly program.
# Goal is to add all @symbols to symbol table, with a corresponding address starting from 16
# Also generates all A and C-command mnemonics and binaries
while not assembly_program.is_parsed():   
    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)

    if command_type == 'A_COMMAND':
        current_command = current_command[1:]

        # Check if the A_COMMAND is a decimal number or a symbol (variable)
        is_decimal = assembly_program.is_decimal(current_command)

        if is_decimal:
            a_command_bin = convert_to_bin(current_command)
        else: # Add symbol to symbol table
            symbol = current_command
            print(symbol)
    else:   # It's a C_COMMAND
        dest_mnemonics = assembly_program.dest_mnemonics(current_command)
        comp_mnemonics = assembly_program.comp_mnemonics(current_command)
        jump_mnemonics = assembly_program.jump_mnemonics(current_command)

        # Generate a Translator object, which contains the converted mnemonics to bits
        mnemonics_to_bin = Translator(dest_mnemonics, comp_mnemonics, jump_mnemonics)

        c_command_bin = '111' + mnemonics_to_bin.comp_bits + \
                        mnemonics_to_bin.dest_bits + mnemonics_to_bin.jump_bits