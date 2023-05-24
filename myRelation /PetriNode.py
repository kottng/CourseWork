class PetriNode:
    def __init__(self, name, node_type, marking=0):
        self.name = name
        self.type = node_type
        self.marking = marking
        self.in_arcs = []
        self.out_arcs = []

    def add_in_arc(self, arc):
        self.in_arcs.append(arc)

    def add_out_arc(self, arc):
        self.out_arcs.append(arc)

    def get_mapping(self):
        return self.mapping

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_in_arcs(self):
        return self.in_arcs

    def get_out_arcs(self):
        return self.out_arcs

    def get_marking(self):
        return self.marking
