# Module translates HACK assembly language mnemonics passed by the parser
# and translates them into binary code.
# Translator contains 3 methods - comp(7bits), dest(3bits) and jump(3bits).

# Examples:
# Command -> Binary representation
# @2 -> 
# D=M ->
# 0;JMP ->


from reference_table import comp_dict_A0, comp_dict_A1, dest_dict, jump_dict

class Translator:
    def __init__(self, dest, comp, jump):
        self.dest = dest
        self.comp = comp
        self.jump = jump


def convert_to_bin(number):
    return f'{int(number):016b}'