# Goal of the parser is to break each assembly command (A or C CPU instruction)
# into its underlying components.
# Reads an assembly language command, parses it and provides convenient access 
# to the command's components (fields and symbols)
# Also, it detects and removes whitespaces and comments

from translator import convert_to_bin
from shutil import copyfile

class Parser:
    def __init__(self, source_file: str):
        self.source_file = source_file              # Loads the source file
        self.assembly_program = self.clean_file()   # Removes comments and whitespaces
        self.is_parsed = self.is_parsed()           # Checks whether the program is parsed
        # self.assembly_file = self.create_file(self.clean_file)

    line_counter = 0

    
    def clean_file(self):
        '''Method removes whitespaces and comments of the provided assembler source file.
        Returns a string to Parser.assembly_program'''

        with open(self.source_file, 'r') as f:
            cleaned_assembler_program = ''

            for line in f:
                if line.startswith('//'):
                    pass
                else:
                    cleaned_assembler_program += line
        
        return cleaned_assembler_program.strip()

    
    def is_parsed(self):
        '''Method stores the number of lines of the assembly program.
        Returns True when the program is parsed, else advances to the next line'''

        assembly_program_length = len(self.assembly_program.split('\n'))   

        while assembly_program_length != Parser.line_counter:
            self.advance()

        return True


    def advance(self):
        '''Method reads the next command from the assembly program and makes it
        the current command. Should only be called while self.is_parsed is False'''

        current_command = self.assembly_program.splitlines()[self.line_counter]
        command_type = self.command_type(current_command)

    
    def command_type(self, command):
        '''Method returns the type of the current CPU command:
            A_COMMAND - for @xxx where xxx is either a symbol or a decimal number;
            C_COMMAND - for dest=comp;jump;
            L_COMMAND - pseudo-command for (XXX) where XXX is a symbol (label);'''
        
        if command.startswith('@') or command.startswith('('):
            # If command starts with '@' or '(' it means we have an A_ or L_COMMAND
            a_command_bin = self.symbol_or_decimal(command)
            print(a_command_bin)
        else:
            pass # Else it is C-command and call something else

        Parser.line_counter += 1
        if self.is_parsed == False:
            self.is_parsed()


    def symbol_or_decimal(self, command):
        '''Method returns the symbol or decimal Xxx of the current command @xxx or (XXX).
        Should only be called if self.command_type() is A_COMMAND or L_COMMAND.
        Converts decimal to binary and returns a string or stores symbol in symbol_table'''

        def check_for_integer(string):
            # Function checks if the A_COMMAND is a symbol or a decimal number
            try:
                int(string)
                return True
            except:
                return False
        
        if command.startswith('@'):
            # Remove the '@' symbol
            a_command = command[1:]
            # Check if the A_COMMAND is a symbol or decimal. 
            is_decimal = check_for_integer(a_command)

            if is_decimal == True:
                # Converts decimal number to 16-bit binary representation
                return convert_to_bin(a_command)
            else:
                pass
        else:
            pass # Else its a label and needs to be added to symbo_table.py


    # def create_file(self, clean_file):
    #     '''Method creates a new file with comments and whitespaces removed'''
    #     with open('/home/uriel/projects-repo/nand2tetris/projects/Assembler/Clean.asm', 'w') as f:
    #         return f.write(clean_file)


parse_file = Parser('/home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm')

# x = parse_file.clean_file

# for line in x.splitlines():
#     print(line)