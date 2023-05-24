from PetriArc import PetriArc
from PetriMapping import PetriMapping
from PetriNet import PetriNet
from PetriNode import PetriNode


def check_subnet_to_place(nodes1, node2, mapping):
    if len(nodes1) > 1:
        list_of_first_vertexes_n1 = []  # массив вершин, которые образуют preset для подсети
        list_of_last_vertexes_n1 = []  # массив вершин, которые образуют postset для подсети
        list_of_first_vertexes_n2 = []  # массив вершин, которые образуют preset для вершины
        list_of_last_vertexes_n2 = []  # массив вершин, которые образуют postset для вершины
        for i in nodes1:
            for j in i.get_in_arcs():
                obj_petri_node = j.get_source()
                if obj_petri_node not in nodes1:
                    list_of_first_vertexes_n1.append(obj_petri_node)
                    # print(obj_petri_node.get_name())
            for j in i.get_out_arcs():
                obj_petri_node = j.get_target()
                if obj_petri_node not in nodes1:
                    list_of_last_vertexes_n1.append(obj_petri_node)
                    # print(obj_petri_node.get_name())
        for i in node2.get_in_arcs():
            obj_petri_node = i.get_source()
            list_of_first_vertexes_n2.append(obj_petri_node)
        for i in node2.get_out_arcs():
            obj_petri_node = i.get_target()
            list_of_last_vertexes_n2.append(obj_petri_node)
        # for i in list_of_first_vertexes_n2:
        #     print(i.get_name())
        # for i in list_of_last_vertexes_n2:
        #     print(i.get_name())
        for i in list_of_first_vertexes_n1:
            if mapping.get_mapped(i)[0] not in list_of_first_vertexes_n2:
                return False
            # print(i.get_name())
        for i in list_of_last_vertexes_n1:
            if mapping.get_mapped(i)[0] not in list_of_last_vertexes_n2:
                return False
            # print(i.get_name())
        if not mapping.is_mapped_acycle(node2):
            return False
        return True


def check_transition_to_place(node1, node2, mapping):
    if node1.type == "transition":
        list_of_in_arcs = node1.get_in_arcs()
        list_of_out_arcs = node1.get_out_arcs()
        list_of_vertexes = []
        for i in list_of_in_arcs:
            list_of_vertexes.append(i.get_source())
        for i in list_of_out_arcs:
            list_of_vertexes.append((i.get_target()))

        for i in list_of_vertexes:
            if mapping.mapped[i][0] != node2:
                return False
    return True


def check_place_to_place(node1, node2, mapping):
    if node1.type == "place":
        list_of_in_arcs_for_node1 = node1.get_in_arcs()
        list_of_out_arcs_for_node1 = node1.get_out_arcs()
        list_of_in_arcs_for_node2 = node2.get_in_arcs()
        list_of_out_arcs_for_node2 = node2.get_out_arcs()
        list_of_in_vertexes_for_node1 = []
        list_of_out_vertexes_for_node1 = []
        mapped_list_of_in_vertexes = []
        mapped_list_of_out_vertexes = []
        list_of_in_vertexes_for_node2 = []
        list_of_out_vertexes_for_node2 = []

        for i in list_of_in_arcs_for_node1:
            list_of_in_vertexes_for_node1.append(i.get_source())

        for i in list_of_out_arcs_for_node1:
            list_of_out_vertexes_for_node1.append(i.get_target())

        for i in list_of_in_arcs_for_node2:
            list_of_in_vertexes_for_node2.append(i.get_source())

        for i in list_of_out_arcs_for_node2:
            list_of_out_vertexes_for_node2.append(i.get_target())

        for i in list_of_in_vertexes_for_node1:
            if mapping.get_mapped(i):
                for j in mapping.get_mapped(i):
                    mapped_list_of_in_vertexes.append(j)
            else:
                print("in arcs to in from ", i.get_name(),
                      " there is a mistake : there is not enough of mapping elements")

        for i in list_of_out_vertexes_for_node1:
            if mapping.get_mapped(i):
                for j in mapping.get_mapped(i):
                    mapped_list_of_out_vertexes.append(j)
            else:
                print("in arcs to out from ", i.get_name(),
                      " there is a mistake : there is not enough of mapping elements")

        for i in mapped_list_of_in_vertexes:
            if i not in list_of_in_vertexes_for_node2:
                return False

        for i in mapped_list_of_out_vertexes:
            if i not in list_of_out_vertexes_for_node2:
                return False

        return True
    else:
        print("it supposed to be place")


def check_transition_to_transition(node1, node2, mapping):
    if node1.type == "transition":
        list_of_in_arcs_for_node1 = node1.get_in_arcs()
        list_of_out_arcs_for_node1 = node1.get_out_arcs()
        list_of_in_arcs_for_node2 = node2.get_in_arcs()
        list_of_out_arcs_for_node2 = node2.get_out_arcs()
        list_of_in_vertexes_for_node1 = []
        list_of_out_vertexes_for_node1 = []
        mapped_list_of_in_vertexes = []
        mapped_list_of_out_vertexes = []
        list_of_in_vertexes_for_node2 = []
        list_of_out_vertexes_for_node2 = []

        for i in list_of_in_arcs_for_node1:
            list_of_in_vertexes_for_node1.append(i.get_source())

        for i in list_of_out_arcs_for_node1:
            list_of_out_vertexes_for_node1.append(i.get_target())

        for i in list_of_in_arcs_for_node2:
            list_of_in_vertexes_for_node2.append(i.get_source())

        for i in list_of_out_arcs_for_node2:
            list_of_out_vertexes_for_node2.append(i.get_target())

        for i in list_of_in_vertexes_for_node1:
            if mapping.get_mapped(i):
                for j in mapping.get_mapped(i):
                    mapped_list_of_in_vertexes.append(j)
            else:
                print("in arcs to in from ", i.get_name(),
                      " there is a mistake : there is not enough of mapping elements")

        for i in list_of_out_vertexes_for_node1:
            if mapping.get_mapped(i):
                for j in mapping.get_mapped(i):
                    mapped_list_of_out_vertexes.append(j)
            else:
                print("in arcs to out from ", i.get_name(),
                      " there is a mistake : there is not enough of mapping elements")

        for i in mapped_list_of_in_vertexes:
            if i not in list_of_in_vertexes_for_node2:
                return False

        for i in mapped_list_of_out_vertexes:
            if i not in list_of_out_vertexes_for_node2:
                return False

        return True
    else:
        print("it supposed to be transitions")


def check_is_transitions_correct(net):
    list_of_transitions = net.transitions
    for i in list_of_transitions.values():
        if len(i.get_in_arcs()) != len(i.get_out_arcs()):
            print("The number of incoming arcs is not equal to the number of outgoing arcs in", i.get_name())
            print("quantity of incoming arcs is: ", len(i.get_in_arcs()))
            print("quantity of outgoing arcs is: ", len(i.get_out_arcs()))
            return False
    return True


def check_is_relation_an_alpha_morphism(net1, net2, mapping):
    if check_is_transitions_correct(net1) and check_is_transitions_correct(net2):
        print("Transitions are okay")
    if not mapping.total_mapping_N2():
        print(" have 0 incoming arcs : Codomain does not have enough incoming arcs")
    else:
        print("mapping for codomain is total")
    if not mapping.total_mapping_N1():
        print(" have 0 or more than 1 outgoing arcs : Domain does not have enough outgoing arcs")
    else:
        print("mapping for domain is total")
    for i in net2.places.values():
        if len(mapping.get_mapping(i)) > 1:
            print(check_subnet_to_place(mapping.get_mapping(i), i, mapping))
        elif mapping.get_mapping(i)[0].get_type() == "place":
            print(check_place_to_place(mapping.get_mapping(i)[0], i, mapping))
        elif mapping.get_mapping(i)[0].get_type() == "transition":
            print(check_transition_to_place(mapping.get_mapping(i)[0], i, mapping))
