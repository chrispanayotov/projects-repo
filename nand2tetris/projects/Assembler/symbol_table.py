# Module keeps correspondence between symbolic labels and numeric addresses

from reference_tables import built_ins_dict

class SymbolTable:
    def __init__(self):
        self.symbol_table = {}
        self.add_builtins = self.symbol_table.update(built_ins_dict)
        

    def add_entry(self, symbol: str, address: int):
        '''Method adds the pair (symbol, address) to the table.'''
        self.symbol_table[symbol] = address


    def contains(self, symbol: str):
        '''Method checks if the symbol table contains the given symbol.
        Returns Boolean'''
        return symbol in self.symbol_table.keys()


    def get_address(self, symbol: str):
        '''Method returns the numeric address associated with the symbol.
        Returns int'''
        return self.symbol_table[symbol]