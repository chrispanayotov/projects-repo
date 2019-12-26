from parser import Parser
from symbol_table import SymbolTable
from translator import Translator, convert_to_bin

# Opens and cleans the source assembly program.
# Exits the program if an invalid path to a file is provided.
source_file = input('Please enter a valid path to a .asm file: ')
assembly_program = Parser(source_file)
translated_program = []

# Create the SymbolTable and add the built-in symbols
symbol_table = SymbolTable()

# Do a first run of the assembly program.
# Scan for (XXX) labels and add them to symbol_table
while not assembly_program.is_parsed():
    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)
    
    if command_type == 'L_COMMAND':
        label_name = current_command[1:len(current_command)-1]

        if not symbol_table.contains_symbol(label_name): 
            symbol_table.add_label(label_name, assembly_program.line_counter)

# Removes all labels from assembly program and restarts it
assembly_program.assembly_program = assembly_program.remove_labels()
assembly_program.line_counter = 0

# Do a second run of the assembly program
# Adds all @symbols to symbol table, with a corresponding address starting from 16
# If the address is already taken increment it by 1 until a free spot in RAM is found
# Generates all A and C-command mnemonics and binaries
while not assembly_program.is_parsed():
    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)

    if command_type == 'A_COMMAND':
        symbol = current_command[1:]

        # Check if the A_COMMAND is a decimal number or a @symbol (variable)
        is_decimal = assembly_program.is_decimal(symbol)

        if is_decimal:
            translated_program.append(convert_to_bin(symbol))
        else:
            symbol_table.add_symbol(symbol)
                
            translated_program.append(convert_to_bin(symbol_table.get_address(symbol)))
    else:   # It's a C_COMMAND
        dest_mnemonics = assembly_program.dest_mnemonics(current_command)
        comp_mnemonics = assembly_program.comp_mnemonics(current_command)
        jump_mnemonics = assembly_program.jump_mnemonics(current_command)

        # Generate a Translator object, 
        # which contains the converted command mnemonics to bits
        mnemonics_to_bin = Translator(dest_mnemonics, comp_mnemonics, jump_mnemonics)

        c_command_bin = '111' + mnemonics_to_bin.comp_bits + \
                        mnemonics_to_bin.dest_bits + mnemonics_to_bin.jump_bits
        
        translated_program.append(c_command_bin)
    
# Get the name of the source file and 
# create a new path leading to a source_file_name.hack file
output_file_name = source_file.split('/')[-1].split('.')[0]
output_file_list = source_file.split('/')
output_file_list[-1] = output_file_name + '.hack'

output_file_path = ''

for line in output_file_list:
    output_file_path += '/' + line

# Create a .hack file with the translated to machine code assembler program
with open(output_file_path, 'w') as f:
    for line in translated_program:
        f.write(line + '\n')