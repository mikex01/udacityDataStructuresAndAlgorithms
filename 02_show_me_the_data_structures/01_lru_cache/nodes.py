# -*- coding: utf-8 -*-
# @autor: Miguel Itzep

# Doble node
class nodes(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
    def __repr__(self):
        if self.value is None:
            return 'None'
        return str(self.value)