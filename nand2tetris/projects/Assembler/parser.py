# Goal of the parser is to break each assembly command (A or C CPU instruction)
# into its underlying components.
# Reads an assembly language command, parses it and provides convenient access 
# to the command's components (fields and symbols)
# Also, it detects and removes whitespaces and comments

from shutil import copyfile

class Parser:
    def __init__(self, source_file: str):
        self.source_file = source_file  # Loads the source file
        self.assembly_program = self.clean_file() # Removes comments and whitespaces
        self.is_parsed = self.is_parsed()   # Checks whether the program is parsed
        self.advance = self.advance()   # Advances to next line in the assembly program
        # self.assembly_file = self.create_file(self.clean_file)

    
    def clean_file(self):
        '''Method removes whitespaces and comments of the provided assembler source file.
        Returns a string to Parser.cleaned_file()'''

        with open(self.source_file, 'r') as f:
            cleaned_assembler_program = ''

            for line in f:
                if line.startswith('//'):
                    pass
                else:
                    cleaned_assembler_program += line
        
        return cleaned_assembler_program.strip()

    
    def is_parsed(self):
        '''Method checks the length of the assembly program and returns True
        if there are more commands to be read. Returns False if the program is finished.'''
        program_length = len(self.assembly_program.split('\n'))
        print(program_length)
        


    def advance(self):
        '''Method reads the next command from the source program and makes it
        the current command. Should only be called if self.has_more_comments() is true'''

        for command in self.assembly_program.splitlines():
            print(command)



    
    def command_type(self):
        '''Method returns the type of the current CPU command:
            A_COMMAND - for @xxx where xxx is either a symbol or a decimal number
            C_COMMAND - for dest=comp;jump
            L_COMMAND - pseudo-command for (XXX) where XXX is a symbol (label)
        '''
        pass

    # def create_file(self, clean_file):
    #     '''Method creates a new file with comments and whitespaces removed'''
    #     with open('/home/uriel/projects-repo/nand2tetris/projects/Assembler/Clean.asm', 'w') as f:
    #         return f.write(clean_file)


parse_file = Parser('/home/uriel/projects-repo/nand2tetris/projects/Assembler/Add.asm')

# x = parse_file.clean_file

# for line in x.splitlines():
#     print(line)