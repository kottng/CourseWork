from myRelation.PetriMapping import PetriMapping
from myRelation.PetriNet import PetriNet
from myRelation.checkRelation import check_is_relation_an_alpha_morphism


# Задание 2 Сетей Петри
# Создаем объект сети Петри
net1 = PetriNet()

# Добавляем места и переходы
net1.add_place("P1")
net1.add_transition("T1")
net1.add_place("P2")
net1.add_transition("T2")
net1.add_place("P3")
net1.add_transition("T3")
net1.add_transition("T4")
net1.add_transition("T5")
net1.add_transition("T6")
net1.add_place("P4")
net1.add_place("P5")
net1.add_place("P6")

# Добавляем дуги

net1.add_arc("P1", "T1")
net1.add_arc("P1", "T2")
net1.add_arc("T1", "P2")
net1.add_arc("T2", "P3")
net1.add_arc("P2", "T3")
net1.add_arc("P3", "T4")
net1.add_arc("T3", "P4")
net1.add_arc("T4", "P5")
net1.add_arc("P4", "T5")
net1.add_arc("P5", "T6")
net1.add_arc("T5", "P6")
net1.add_arc("T6", "P6")

# Получаем вершину P1
p1 = net1.places["P1"]

# Получаем список исходящих дуг из вершины P1
out_arcs = p1.get_in_arcs()
# Проходимся по списку и выводим целевые вершины
for arc in out_arcs:
    target_node = arc.get_source()

# Создаем другой объект сети Петри
net2 = PetriNet()

# Добавляем места и переходы
net2.add_place("Q1")
net2.add_transition("R1")
net2.add_place("Q2")
net2.add_transition("R2")
net2.add_place("Q3")
# Добавляем дуги

net2.add_arc("Q1", "R1")
net2.add_arc("R1", "Q2")
net2.add_arc("Q2", "R2")
net2.add_arc("R2", "Q3")

# Получаем вершину P1
q1 = net2.places["Q1"]
# Получаем список исходящих дуг из вершины P1
out_arcs = q1.get_in_arcs()
# Проходимся по списку и выводим целевые вершины
for arc in out_arcs:
    target_node = arc.get_source()

mapping = PetriMapping(net1, net2)
list_of_places1 = []
list_of_places2 = []
list_of_transitions1 = []
list_of_transitions2 = []

for i in net1.places.values():
    list_of_places1.append(i)

for i in net1.transitions.values():
    list_of_transitions1.append(i)

for i in net2.transitions.values():
    list_of_transitions2.append(i)

for i in net2.places.values():
    list_of_places2.append(i)

mapping.add_mapping(list_of_places1[0], list_of_places2[0])
mapping.add_mapping(list_of_places1[5], list_of_places2[2])
mapping.add_mapping(list_of_transitions1[0], list_of_transitions2[0])
mapping.add_mapping(list_of_transitions1[1], list_of_transitions2[0])
mapping.add_mapping(list_of_places1[1], list_of_places2[1])
mapping.add_mapping(list_of_places1[2], list_of_places2[1])
mapping.add_mapping(list_of_transitions1[2], list_of_places2[1])
mapping.add_mapping(list_of_transitions1[3], list_of_places2[1])
mapping.add_mapping(list_of_places1[3], list_of_places2[1])
mapping.add_mapping(list_of_places1[4], list_of_places2[1])
mapping.add_mapping(list_of_transitions1[4], list_of_transitions2[1])
mapping.add_mapping(list_of_transitions1[5], list_of_transitions2[1])
# mapping.add_mapping(list_of_places1[2], list_of_places2[0])
check_is_relation_an_alpha_morphism(net1, net2, mapping)
