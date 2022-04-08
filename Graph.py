from collections import OrderedDict

class Graph():
    def __init__(self, is_directed):
        super(Graph, self).__init__()
        self.is_directed = is_directed
        self.graph = {}
        self.matrix = []
        self.subgraphs = []

    def add_vertex(self, vertex):
        # Adiciona nova chave (vértice) ao dicionário
        self.graph.update({vertex: []})

    def add_connection(self, vertex_name, connections):
        # Se o próprio vértice está nas conexões
        if vertex_name in connections:
            print(
                "Um vértice não pode fazer conexão com ele mesmo,",
                f"a conexão '{vertex_name}' foi removida"
            )
            connections.remove(str(vertex_name))
        # Converte as conexões para lista se vierem como string
        
        if isinstance(connections, str):
            connections = connections.lower().replace(' ', '').split(',')
        
        for invalid_connection in ['\n', '\t', '\r', ' ', '']:
            if invalid_connection in connections:
                connections.remove(invalid_connection)
        
        if self.is_directed is False:  # Se for não-dirigido

            # Adiciona as conexões ao vértice
            self.graph[vertex_name] = list(
                self.graph[vertex_name] + connections
            )
            self.graph[vertex_name]=list(OrderedDict.fromkeys(self.graph[vertex_name]))
            """ Adiciona o vértice como uma conexão para cada um dos vértices
            que ele fez conexão """
            for connection in connections:
                # Se não for uma conexão vazia
                if connection not in ['\n', '\t', '\r', ' ', '']:
                    self.graph[connection] = list(
                        self.graph[connection] + [vertex_name]
                    )
                    self.graph[connection]=list(OrderedDict.fromkeys(self.graph[connection]))
        else:  # Se for dirigido]
           
            for connection in connections:
                # Se não for uma conexão vazia
                if connection not in ['\n', '\t', '\r', ' ', '']:
                    """ Só adiciona a conexão se o vértice não for uma conexão
                    do vértice que ele deseja conectar """
                    if vertex_name not in self.graph[connection]:
                        self.graph[vertex_name] = list(
                            self.graph[vertex_name] + [connection]
                        )
                        self.graph[vertex_name]=list(OrderedDict.fromkeys(self.graph[vertex_name]))
                    else:
                        print(
                            f"O vértice '{connection}' já faz conexão com o",
                            f"vértice '{vertex_name}' (O Grafo é Dirigido!)"
                        )

    def remove_vertex(self, vertex_name):
        # Remove a chave (vértice) do dicionário
        self.graph.pop(vertex_name)
        # Percorre os vértices e suas conexões
        for vertex, connections in self.graph.items():
            # Remove o vértice das conexões em que ele aparece
            if vertex_name in connections:
                self.graph[vertex].remove(vertex_name)

    def remove_vertex_copy(self, graph_copy, vertex_name):
        # Remove a chave (vértice) do dicionário
        graph_copy.pop(vertex_name)
        # Percorre os vértices e suas conexões
        for vertex, connections in graph_copy.items():
            # Remove o vértice das conexões em que ele aparece
            if vertex_name in connections:
                graph_copy[vertex].remove(vertex_name)
        return graph_copy
        
    def remove_connection(self, vertex_name, connections):
        for connection in connections:
            # Acessa o vértice e remove a conexão
            self.graph[str(vertex_name)].remove(str(connection))
            # Se o grafo for não-dirigido ele remove a conexão dos dois lados
            if self.is_directed is False:
                self.graph[str(connection)].remove(str(vertex_name))

    def DFS_search(self, location, wanted):  # Busca em profundidade
        
        # Lista de visitados
        visited_DFS = []
        # Adiciona o vértice inicial na lista de visitados
        visited_DFS.append(location)
        # Contador auxiliar
        count = 2

        # Enquanto não visitou todos os vértices
        while len(visited_DFS) != len(self.graph) and location != wanted:
            # Primeira conexão não visitada ainda, no vértice atual
            valor = next((
                connection for connection in self.graph[location]
                if connection not in visited_DFS),
                None
            )
            # Se todas as conexões são vértices já visitados
            if valor is None:
                """ Se já passou por todas as conexões de todos os vértices
                    da lista de visitados mas ainda restam vértices não
                    visitados no grafo """
                if (len(visited_DFS) - count) == -2:
                    # Procura por um vértice não visitado
                    location = next((
                        vertex for vertex in self.graph.keys()
                        if vertex not in visited_DFS)
                    )
                    # Visita o vértice
                    visited_DFS.append(location)

                else:
                    # Acessa as conexões do vértice anterior da pilha
                    location = visited_DFS[len(visited_DFS) - count]
                    # Aumenta o contador, indicando que voltou um item da pilha
                    count += 1
            else:
                # Contador volta ao valor inicial, topo da pilha
                count = 2
                # Visita o vértice
                visited_DFS.append(valor)
                location = valor

        print('Busca em Profundidade: ', visited_DFS)

    def BFS_search(self, location, wanted):  # Busca em largura
        # Lista de visitados
        visited_BFS = []
        # Adiciona o vértice inicial na lista de visitados
        visited_BFS.append(location)

        # Adiciona os adjacentes do vértice inicial
        visited_BFS.extend(self.graph[location])
        count = 1

        # Primeiro adjacente vira vértice inicial
        location = visited_BFS[count]

        # Enquanto não visitou todos os vértices
        while len(visited_BFS) != len(self.graph) and wanted not in visited_BFS:
            # Lista com todos os adjacentes não visitados do vértice atual
            connections_non_visited = [
                vertex for vertex in self.graph[location]
                if vertex not in visited_BFS
            ]

            # Se todos os adjacentes do vértice atual já foram visitados
            if connections_non_visited == []:
                # Próximo vértice da lista
                count += 1
                """ Se já passou por todas as conexões de todos os
                    vértices da lista mas ainda restam vértices não
                    visitados no grafo """
                if len(visited_BFS) == count:
                    # Procura por um vértice não visitado
                    location = next((
                        vertex for vertex in self.graph.keys()
                        if vertex not in visited_BFS))
                    # Visita o vértice
                    visited_BFS.append(location)
                else:
                    # Visita o próximo vértice não visitado da lista
                    location = visited_BFS[count]
            else:
                """ Incrementa o contador (apontando para o próximo
                vértice da lista) """
                count += 1
                # Visita o próximo adjacente não visitado do vértice atual
                location = connections_non_visited[0]
            # Adiciona adjacentes não visitados à lista
            visited_BFS.extend(connections_non_visited)

        if wanted is not None:
            visited_BFS = visited_BFS[:visited_BFS.index(wanted) + 1]
        print('Busca em Largura: ', visited_BFS)
   
    def inv_transitive_closure(self, location, graph_copy):
        initial = location
        visited = [location]
        stack = []
        while True:
            for vertex, connections in graph_copy.items():
                if location in connections and vertex not in visited and vertex not in stack:
                    stack.append(vertex)
            if stack == []:
                print(f'Fecho transitivo inverso do vértice {initial}: {visited}')
                return visited
            location = stack[0]
            visited.append(location)
            del stack[0]

    def dir_transitive_closure(self, location, graph_copy):
        initial = location
        # Lista de visitados
        visited = []
        
        # Adiciona o vértice inicial na lista de visitados
        visited.append(location)

        # Adiciona os adjacentes do vértice inicial
        visited.extend(graph_copy[location])
        count = 1

        # Primeiro adjacente vira vértice inicial
        location = visited[count]

        # Enquanto não visitou todos os vértices
        while len(visited) != len(graph_copy):
            # Lista com todos os adjacentes não visitados do vértice atual
            connections_non_visited = [
                vertex for vertex in graph_copy[location]
                if vertex not in visited
            ]

            # Se todos os adjacentes do vértice atual já foram visitados
            if connections_non_visited == []:
                print(f"Fecho transitivo direto do vértice {initial}: {visited}")
                return visited
            else:
                """ Incrementa o contador (apontando para o próximo
                vértice da lista) """
                count += 1
                # Visita o próximo adjacente não visitado do vértice atual
                location = connections_non_visited[0]
                

            # Adiciona adjacentes não visitados à lista
            visited.extend(connections_non_visited)

        print(f'Fecho transitivo direto do vértice {initial}: {visited}')
        return visited
    

    def intersection(self, dir, inv):
        inter = [value for value in dir if value in inv]
        return inter

    def getSubgraphConnections(self, subgraph, graph_copy):
        subgraph_dict = {}
        for vertex in subgraph:
            connections = graph_copy[vertex]
            connections = [item for item in connections if item in subgraph]
            subgraph_dict[vertex] = connections

        return subgraph_dict


    def is_connected(self, location):
        # TRANSFORMAR EM EXECUTAVEL
        # APLICAR LARGURA E PROFUNDIDADE?
        # LISTAR TODOS OS SUBGRAFOS NO FINAL
        # REMOVER OS VERTICES QUE JA FORAM NA HORA DE FAZER O FECHO TRANSITIVO DIRETO 
        
        graph_copy = self.graph.copy()
        self.subgraphs = []

        dir = self.dir_transitive_closure(location, graph_copy)
        inv = self.inv_transitive_closure(location, graph_copy)
        subgraph = self.intersection(dir, inv)

        if set(subgraph) == set(graph_copy.keys()):  # Verifica se já contém todos os vértices do grafo
            print('GRAFO CONEXO!')
            return
        else:
            print('GRAFO DESCONEXO!')

            subgraph = self.getSubgraphConnections(subgraph, graph_copy)

            self.subgraphs.append(subgraph)
            print(f'Subgrafo 1 (vértice {location}): {subgraph}')

            for item in subgraph:
                graph_copy = self.remove_vertex_copy(graph_copy, item)

            count = 2
            while list(graph_copy.keys()) != []:
                location = input(f'Escolha um vértice para encontrar o próximo subgrafo ({list(graph_copy.keys())}): ')
                while location not in list(graph_copy.keys()):
                    print('Valor inválido, insira novamente')
                    location = input(f'Escolha um vértice para encontrar o próximo subgrafo ({list(graph_copy.keys())}): ')
                
                dir = self.dir_transitive_closure(location, graph_copy)
                inv = self.inv_transitive_closure(location, graph_copy)
                subgraph = self.intersection(dir, inv)

                

                subgraph = self.getSubgraphConnections(subgraph, graph_copy)
                self.subgraphs.append(subgraph)
                print(f'Subgrafo {count} (vértice {location}): {subgraph}')
                
                for item in subgraph:
                    graph_copy = self.remove_vertex_copy(graph_copy, item)
                    
                count += 1
        










    
        

    def generate_matrix(self):
        # Zera a matriz
        self.matrix = []
        # Adiciona os nomes das colunas (vértices)
        self.matrix.append([' '] + list(self.graph.keys()))
        # Percorre os vértices e suas conexões
        for vertex, connections in self.graph.items():
            # Adiciona o nome do vértice na linha
            line = [vertex]
            # Verifica as conexões do vértice atual com os demais
            for aux_vertex in self.graph.keys():
                """ Adiciona 1 à linha se o vértice estiver nas conexões do
                vértice atual e 0 se não estiver """
                line.append(1) if aux_vertex in connections else line.append(0)
            self.matrix.append(line)

    def print_matrix(self):
        print('Matriz:')

        # Percorre a matriz imprimindo seus valores
        for row in self.matrix:
            for i in row:
                print(i, end=' | ')
            print('')
            print()
