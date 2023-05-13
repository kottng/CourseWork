


class PetriMapping:
    def __init__(self, domain_net, codomain_net):
        self.mapping = {}
        self.mapped = {}
        self.domain_net = domain_net
        self.codomain_net = codomain_net

    def add_mapping(self, node1, node2):
        if node1.type == "place" and node2.type == "transition":
            raise ValueError("place can't be mapped to transition")
        elif node1.get_marking() != node2.get_marking():
            raise ValueError("markings for ", node1.name, " and ", node2.name, " are different")
        else:
            if node2 not in self.mapping:
                self.mapping[node2] = []
            self.mapping[node2].append(node1)
            if node1 not in self.mapped:
                self.mapped[node1] = []
            self.mapped[node1].append(node2)

    def get_mapping(self, node):
        return self.mapping.get(node)

    def get_mapped(self, node):
        return self.mapped.get(node)

    def total_mapping_N2(self):
        for place2 in self.codomain_net.places.values():
            if place2 not in self.mapping:
                return False
        return True

    def total_mapping_N1(self):
        for place1 in self.domain_net.places.values():
            if place1 not in self.mapped or len(self.mapped.get(place1)) > 1:
                return False
        return True

    def is_mapped_acycle(self, node):
        list_of_vertexes = self.mapping[node]
        # print(list_of_vertexes)
        visited = {}
        for i in list_of_vertexes:
            visited[i] = False
        a = 0
        for i in list_of_vertexes:
            if not visited[i]:
                if self.dfs(list_of_vertexes, list_of_vertexes[a], visited):
                    return True
            a += 1
        return False

    def dfs(self, list_of_vertexes, vertex, visited):
        # print("________")
        # print(vertex)
        visited[vertex] = True
        for ver in vertex.get_out_arcs():
            ver = ver.get_target()
            # print(ver)
            if ver in list_of_vertexes:
                if visited[ver]:
                    return False
                else:
                    return self.dfs(list_of_vertexes, ver, visited)
        return True

    def check_transition_to_place(self, node1, node2):
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

    def check_place_to_place(self, node1, node2):
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
                    raise ValueError("in arcs to in from ", i.get_name(), " there is a mistake : there is not enough of mapping elements")

            for i in list_of_out_vertexes_for_node1:
                if mapping.get_mapped(i):
                    for j in mapping.get_mapped(i):
                        mapped_list_of_out_vertexes.append(j)
                else:
                    raise ValueError("in arcs to out from ", i.get_name(), " there is a mistake : there is not enough of mapping elements")


            for i in mapped_list_of_in_vertexes:
                if i not in list_of_in_vertexes_for_node2:
                    return False

            for i in mapped_list_of_out_vertexes:
                if i not in list_of_out_vertexes_for_node2:
                    return False

            return True
        else:
            raise ValueError("it supposed to be place")