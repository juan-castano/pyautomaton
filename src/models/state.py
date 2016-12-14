"""
State for Automaton
"""

class State(object):

    def __init__(self, id="", is_acceptor=False, is_initial=False, transitions_table={}):
        self.id = id
        self.is_acceptor = is_acceptor
        self.is_initial = is_initial
        self.transitions_table = transitions_table

    def __str__(self):
        return 
            "[" + \
            "ID: " + self.id + \ 
            " - is acceptor: " + self.is_acceptor + \ 
            " - is initial: " + self.is_initial + \
            " - transitions table " + str(self.transitions_table) + \
            "]"