import time
from parser import Parser
from symbol_table import SymbolTable
from translator import Translator, convert_to_bin

start_time = time.time()

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
    command_type = assembly_program.get_command_type(current_command)
    
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
    command_type = assembly_program.get_command_type(current_command)

    if command_type == 'A_COMMAND':
        symbol = current_command[1:]

        # Check if the A_COMMAND is a decimal number or a @symbol (variable)
        if assembly_program.is_decimal(symbol):
            translated_program.append(convert_to_bin(symbol))
        elif not symbol_table.contains_symbol(symbol):
            symbol_table.add_symbol(symbol)
            translated_program.append(convert_to_bin(symbol_table.get_address(symbol)))
        else:
            translated_program.append(convert_to_bin(symbol_table.get_address(symbol)))

    else:   # It's a C_COMMAND
        dest_mnemonics = assembly_program.get_dest_mnemonics(current_command)
        comp_mnemonics = assembly_program.get_comp_mnemonics(current_command)
        jump_mnemonics = assembly_program.get_jump_mnemonics(current_command)

        # Generate a Translator object, 
        # which contains the converted command mnemonics to bits
        mnemonics_to_bin = Translator(dest_mnemonics, comp_mnemonics, jump_mnemonics)

        c_command_bin = '111' + mnemonics_to_bin.comp_bits + \
                        mnemonics_to_bin.dest_bits + mnemonics_to_bin.jump_bits
        
        translated_program.append(c_command_bin)


def get_output_file_path(source_file):    
    # Function gets the name and path of the source file
    output_file_name = source_file.split('/')[-1].split('.')[0]
    output_file_list = source_file.split('/')
    output_file_list[-1] = output_file_name + '_python.hack'
    output_file_path = ''

    for line in output_file_list:
        output_file_path += '/' + line
    
    return output_file_path


def create_output_file(path_name):
# Create a .hack file with the translated to machine code assembler program
    with open(path_name, 'w') as f:
        for line in translated_program:
            f.write(line + '\n')


output = get_output_file_path(source_file)
create_output_file(output)

print(f'Assembly program successfuly parsed in {time.time() - start_time:.2f} seconds')