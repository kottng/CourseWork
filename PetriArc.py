class PetriArc:
    def __init__(self, source_node, target_node):
        self.source = source_node
        self.target = target_node

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target
