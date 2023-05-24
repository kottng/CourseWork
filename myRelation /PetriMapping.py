class PetriMapping:

    def __init__(self, domain_net, codomain_net):
        self.mapping = {}
        self.mapped = {}
        self.domain_net = domain_net
        self.codomain_net = codomain_net

    def add_mapping(self, node1, node2):
        if node1.type == "place" and node2.type == "transition":
            print(node1.get_name(), "place can't be mapped to transition", node2.get_name())
        elif node1.get_marking() != node2.get_marking():
            print("markings for ", node1.name, " and ", node2.name, " are different")
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
                # print(place2.get_name(), end='')
                return False
        return True

    def total_mapping_N1(self):
        for place1 in self.domain_net.places.values():
            # print(place1.get_name(),  len(self.mapped.get(place1)))
            if place1 not in self.mapped or len(self.mapped.get(place1)) > 1:
                # print(place1.get_name(), end='')
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
