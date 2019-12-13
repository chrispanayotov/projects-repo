from parser import Parser
from symbol_table import SymbolTable
from translator import Translator, convert_to_bin

# /home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm

# Opens and cleans the source file. 
# source_file = input('Please enter a valid path to .asm file ')
assembly_program = Parser('/home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm')

# Create the SymbolTable
symbol_table = SymbolTable()
times_scanned = 0


# Do a first run of the assembly program.
# Goal is to scan the progam for LABELS and them to symbol table
# After the first run is complete removes all (XXX) labels from assembly program
while times_scanned == 0:    
    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)
    
    if command_type == 'L_COMMAND':
        label = current_command[1:len(current_command)-1]

        if not symbol_table.contains(label):
            # Adds label and corresponding address (line number) to symbol table 
            symbol_table.add_entry(label, assembly_program.line_counter)
            print(symbol_table.symbol_table)
        
    if assembly_program.is_parsed():
        times_scanned += 1

# Do a second run of the assembly program.
# Goal is to add all @symbols to symbol table, with a corresponding address starting from 16
# Also generates all A and C-command mnemonics and binaries
while times_scanned == 1:   
    if command_type == 'A_COMMAND':
        # Check if the A_COMMAND is a decimal number or a symbol (variable)
        is_decimal = assembly_program.is_decimal(current_command)

        if is_decimal:
            a_command_bin = convert_to_bin(current_command[1:])
        else:
            pass
            # Add to symbol_table
    else:   #Else its a C_COMMAND
        dest_mnemonics = assembly_program.dest_mnemonics(current_command)
        comp_mnemonics = assembly_program.comp_mnemonics(current_command)
        jump_mnemonics = assembly_program.jump_mnemonics(current_command)

        # Generate a Translator object, which contains the converted mnemonics to bits
        mnemonics_to_bin = Translator(dest_mnemonics, comp_mnemonics, jump_mnemonics)

        c_command_bin = '111' + mnemonics_to_bin.comp_bits + \
                        mnemonics_to_bin.dest_bits + mnemonics_to_bin.jump_bits

    if assembly_program.is_parsed():
        times_scanned += 1