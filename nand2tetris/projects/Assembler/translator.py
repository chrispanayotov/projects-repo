# Module translates HACK assembly language mnemonics passed by the parser
# and translates them into binary code.
# Translator 
# Translator contains 3 methods - comp(7bits), dest(3bits) and jump(3bits).


class Translator:
    def __init__(self, comp: str, dest: str, jump: str):
        self.comp = comp #