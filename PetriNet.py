
from PetriArc import PetriArc
from PetriMapping import PetriMapping
from PetriNet import PetriNet
from PetriNode import PetriNode

class PetriNet:
    def __init__(self):
        self.places = {}
        self.transitions = {}
        self.arcs = []

    def add_place(self, name, marking=0):
        self.places[name] = PetriNode(name, "place", marking)

    def add_transition(self, name):
        self.transitions[name] = PetriNode(name, "transition")

    def add_arc(self, source_name, target_name):
        source_node = self.places.get(source_name) or self.transitions.get(source_name)
        target_node = self.places.get(target_name) or self.transitions.get(target_name)

        if len(self.arcs) > 0:
            if target_node.get_type() == source_node.get_type():
                raise ValueError("Two nodes of the same type can't be added in a row")

        arc = PetriArc(source_node, target_node)
        source_node.add_out_arc(arc)
        target_node.add_in_arc(arc)
        self.arcs.append(arc)