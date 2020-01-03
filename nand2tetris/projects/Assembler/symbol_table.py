# Module keeps correspondence between symbolic labels/variables and numeric addresses
# Class SymbolTable has methods for adding a symbol-address entry, 
# checking if a symbol is already in the table, and getting an int address

from reference_tables import built_ins_dict

class SymbolTable:
    def __init__(self):
        self.symbol_table = {}
        self.add_builtins = self.symbol_table.update(built_ins_dict)
        
    variable_address = 16

    def add_label(self, label: str, address: int):
        '''Method adds the pair (LABEL, address) to the table.'''

        self.symbol_table[label] = address

    
    def add_symbol(self, symbol: str):
        '''Method searches for a free address spot in the RAM and 
        adds the pair (symbol, address) to the table'''

        while self.contains_address(self.variable_address):
            if self.variable_address == 16384:
                self.variable_address = 24576
            self.variable_address += 1

        self.add_label(symbol, self.variable_address)


    def contains_symbol(self, symbol: str):
        '''Method checks if the symbol table contains the given symbol.
        Returns bool'''

        return symbol in self.symbol_table.keys()
    

    def contains_address(self, address: int):
        '''Method checks if the symbol table contains the given address
        Returns bool'''
        
        return address in self.symbol_table.values()


    def get_address(self, symbol: str):
        '''Method returns the numeric address associated with the symbol.
        Returns int'''

        return self.symbol_table[symbol]