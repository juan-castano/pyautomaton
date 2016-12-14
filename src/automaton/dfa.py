"""
Deterministic Finite Automaton
"""

class DFA(object):

    def __init__(self, input_string="", states_list=[]):
        self.input_string = input_string
        self.states_list = states_list
    
    def __str__(self):
        pass