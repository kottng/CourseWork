
from myRelation.PetriArc import PetriArc

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
        """Добавляет дугу в сеть Петри.

        Аргументы:
        - source_name (str): Имя исходного узла дуги.
        - target_name (str): Имя целевого узла дуги.

        Выполняет добавление дуги в сеть Петри. Исходный и целевой узлы определяются по их именам.
        Если исходный или целевой узел не существует в сети Петри, выводится ошибка.

        Если в сети Петри уже присутствуют дуги, проверяется тип целевого узла и исходного узла.
        Если они имеют одинаковый тип (оба являются либо позициями, либо переходами), выводится ошибка.

        Создается объект PetriArc, представляющий дугу, и добавляется в списки исходящих дуг для исходного узла
        и входящих дуг для целевого узла. Затем дуга добавляется в список дуг сети Петри.

        """
        source_node = self.places.get(source_name) or self.transitions.get(source_name)
        target_node = self.places.get(target_name) or self.transitions.get(target_name)

        if len(self.arcs) > 0:
            if target_node.get_type() == source_node.get_type():
                print("Two nodes of the same type can't be added in a row")

        arc = PetriArc(source_node, target_node)
        source_node.add_out_arc(arc)
        target_node.add_in_arc(arc)
        self.arcs.append(arc)
