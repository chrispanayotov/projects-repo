# Module contains dictionaries for each of the three fields:
# computation, destination and jump to their binary forms
# Goal is to be used for reference for the Translator module so
# it can convert CPU commands to binary

# C-Command binary: 111a c1c2c3c4 c5c6d1d2 d3j1j2j3
# Each key-value pair is stored as a string

# Dictionary for computation bits c1c2c3c4c5c6, when comp (a=0)
comp_dict_A0 = {
    '0': '101010',
    '1': '111111',
    '-1': '111010',
    'D': '001100',
    'A': '110000', 
    '!D': '001101',
    '!A': '110001',
    '-D': '001111',
    '-A': '110011',
    'D+1': '011111',
    'A+1': '110111',
    'D-1': '001110',
    'A-1': '110010',
    'D+A': '000010',
    'D-A': '010011',
    'A-D': '000111',
    'D&A': '000000',
    'D|A': '010101'
}

# Dictionary for when comp (a=1)
comp_dict_A1 = {
    'M': '110000',
    '!M': '110001',
    '-M': '110011',
    'M+1': '110111',
    'M-1': '110010',
    'D+M': '000010',
    'D-M': '010011',
    'M-D': '000111',
    'D&M': '000000',
    'D|M': '010101'
}

# Dictionary for the destination bits d1d2d3
dest_dict = {
    None: '000',
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111'
}

# Dictionary for the jump bits j1j2j3
jump_dict = {
    None: '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111'
}