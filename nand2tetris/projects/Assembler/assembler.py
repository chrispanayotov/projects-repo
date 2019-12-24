from parser import Parser
from symbol_table import SymbolTable
from translator import Translator, convert_to_bin

# /home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm

source_file = input('Please enter a valid path to a .asm file: ')

# Opens and cleans the file. Exits the program if an invalid path is provided.
assembly_program = Parser(source_file)
translated_program = []

print(assembly_program.assembly_program)

# Create the SymbolTable and add the built-ins
symbol_table = SymbolTable()

# Do a first run of the assembly program.
# Scans the progam for LABELS and add them to symbol table
while not assembly_program.is_parsed():
    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)
    
    if command_type == 'L_COMMAND':
        # Get the labels name
        label = current_command[1:len(current_command)-1]

        if not symbol_table.contains_symbol(label):
            # Adds label and corresponding address (line number) to symbol table 
            symbol_table.add_entry(label, assembly_program.line_counter)
        


# After the first run is complete removes all (XXX) labels from assembly program 
# and start from the beginning of program
assembly_program.assembly_program = assembly_program.remove_labels()
assembly_program.line_counter = 0

print(symbol_table.symbol_table)


# Do a second run of the assembly program.
# Adds all @symbols to symbol table, with a corresponding address starting from 16
# Also generates all A and C-command mnemonics and binaries
while not assembly_program.is_parsed():
    variable_address = 16

    current_command = assembly_program.advance()
    command_type = assembly_program.command_type(current_command)

    if command_type == 'A_COMMAND':
        current_command = current_command[1:]

        # Check if the A_COMMAND is a decimal number or a symbol (variable)
        is_decimal = assembly_program.is_decimal(current_command)

        if is_decimal:
            translated_program.append(convert_to_bin(current_command))
        else:
            # Check if symbol is in table, if it's not add it
            symbol = current_command

            # Check how to loop through symbol_tables' values and to check if the current
            # variable_address number is already there as a LABEL. If it is increment
            # variable_address by 1, until a free spot in the RAM is found
            
            # if symbol_table.contains_symbol(symbol) == False and symbol_table.contains_address == False:
            #     symbol_table.add_entry(symbol, variable_address)
            #     variable_address += 1
            # else:
            #     variable_address += 1



            # symbol_address = symbol_table.get_address(symbol)
            # translated_program.append(convert_to_bin(symbol_address))
    else:   # It's a C_COMMAND
        dest_mnemonics = assembly_program.dest_mnemonics(current_command)
        comp_mnemonics = assembly_program.comp_mnemonics(current_command)
        jump_mnemonics = assembly_program.jump_mnemonics(current_command)

        # Generate a Translator object, which contains the converted mnemonics to bits
        mnemonics_to_bin = Translator(dest_mnemonics, comp_mnemonics, jump_mnemonics)

        c_command_bin = '111' + mnemonics_to_bin.comp_bits + \
                        mnemonics_to_bin.dest_bits + mnemonics_to_bin.jump_bits
        
        translated_program.append(c_command_bin)


# Get the name of the source file and create a new path leading to a source_file_name.hack file
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