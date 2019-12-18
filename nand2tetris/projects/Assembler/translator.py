# Module translates HACK assembly language mnemonics passed by the parser
# and translates them into binary code.
# Translator contains 3 methods - comp(7bits), dest(3bits) and jump(3bits).
# Module also has a side-function convert_to_bin, because I think this is the 
# best place for it.

# Examples:
# Command -> Binary representation:
    # @2 -> 0000000000000010
    # D=A -> 1110110000010000
    # 0;JMP -> 1110101010000111

from reference_tables import comp_dict_A0, comp_dict_A1, dest_dict, jump_dict

class Translator:
    def __init__(self, dest, comp, jump):
        self.dest_bits = self.dest_to_bin(dest)
        self.comp_bits = self.comp_to_bin(comp)
        self.jump_bits = self.jump_to_bin(jump)
    

    def dest_to_bin(self, dest_mnemonics):
        return dest_dict[dest_mnemonics]


    def comp_to_bin(self, comp_mnemonics):
        comp_bits = ''

        if comp_mnemonics in comp_dict_A1.keys():
            # Set the a-bit in the comp bits to 1 or 0 depending on the command
            comp_bits += '1' + comp_dict_A1[comp_mnemonics]
        else:
            comp_bits += '0' + comp_dict_A0[comp_mnemonics]
        
        return comp_bits
            

    def jump_to_bin(self, jump_mnemonics):
        return jump_dict[jump_mnemonics]


def convert_to_bin(number):
    # Converts A_COMMAND decimal number to 16-bit binary
    return f'{int(number):016b}'