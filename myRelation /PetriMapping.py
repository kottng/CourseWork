class PetriMapping:

    def __init__(self, domain_net, codomain_net):
        self.mapping = {}
        self.mapped = {}
        self.domain_net = domain_net
        self.codomain_net = codomain_net

    def add_mapping(self, node1, node2):
        """Добавляет отображение между двумя вершинами в отображении.

        Аргументы:
        - node1: PetriNode - первая вершина
        - node2: PetriNode - вторая вершина

        Добавляет отображение между вершинами `node1` и `node2` в отображении `mapping`.
        Проверяет тип вершин и их маркировку. Если типы вершин не соответствуют ("place" и "transition")
        или маркировки вершин отличаются, выводит соответствующие сообщения об ошибке.
        В противном случае, добавляет вершины в отображение `mapping` и `mapped`, где mapping - словарь для кодомейна,
        а mapped - словарь для домейна.

        """
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
        """Проверяет, является ли отображение тотальным для кодомейна.

        Возвращает:
        - bool: True, если отображение полное для всех мест в кодомейне, иначе False.

        Проверяет, содержит ли отображение `mapping` отображения для всех мест (`place2`)
        в кодомейн. Если какое-либо место в кодомейне не имеет отображения, возвращает False.
        В противном случае, возвращает True.

        """
        for place2 in self.codomain_net.places.values():
            if place2 not in self.mapping:
                return False
        return True

    def total_mapping_N1(self):
        """Проверяет, является ли отображение тотальным для домейна.

        Возвращает:
        - bool: True, если отображение полное для всех мест в домейне, иначе False.

        Проверяет, содержит ли отображение `mapping` отображения для всех мест (`place2`)
        в домейне. Если какое-либо место в домейне не имеет отображения, возвращает False.
        В противном случае, возвращает True.

        """
        for place1 in self.domain_net.places.values():
            # print(place1.get_name(),  len(self.mapped.get(place1)))
            if place1 not in self.mapped or len(self.mapped.get(place1)) > 1:
                # print(place1.get_name(), end='')
                return False
        return True

    def is_mapped_acycle(self, node):
        """Проверяет, является ли подграф отображения связным и ацикличным. Для этого используется вспомогательная функция `dfs`

        Аргументы:
        - node (PetriNode): Узел, для которого выполняется проверка.

        Возвращает:
        - bool: True, если подграф отображения, состоящий из узлов, соответствующих `node`,
          является связным и ацикличным, иначе False.

        """
        list_of_vertexes = self.mapping[node]
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
        """Выполняет обход в глубину для проверки ацикличности подграфа отображения.

        Аргументы:
        - list_of_vertexes (list): Список узлов, в которых выполняется обход.
        - vertex (PetriNode): Текущий узел, для которого выполняется обход.
        - visited (dict): Словарь, хранящий информацию о посещенных узлах.

        Возвращает:
        - bool: True, если обход в глубину не обнаружил циклов, иначе False.

        Функция выполняет обход в глубину для проверки ацикличности подграфа отображения.
        Производит рекурсивные вызовы для каждого соседнего узла `ver`, который является целью
        исходящей дуги из текущего узла `vertex`. Если обнаружен цикл (узел `ver` уже посещен),
        функция возвращает False. В противном случае, продолжает обход до всех соседних узлов.
        Если обход не обнаружил циклов, возвращает True.

        """
        visited[vertex] = True
        for ver in vertex.get_out_arcs():
            ver = ver.get_target()
            if ver in list_of_vertexes:
                if visited[ver]:
                    return False
                else:
                    return self.dfs(list_of_vertexes, ver, visited)
        return True
