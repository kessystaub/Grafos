from Graph import Graph
import re


class App():
    def __init__(self):
        super(App, self).__init__()
        self.vertexes = []

    def get_valid_entry(self, input_message, regex):
        # Valida o input do usuário de acordo com uma expressão regular
        while True:
            entry = input(input_message)
            match = re.search(regex, entry)
            if match:
                return entry
            else:
                print('Valor inválido, por favor digite novamente')

    def user_graph_config(self):
        # Usuário configura o grafo

        # Dirigido ou não dirigido
        is_directed = self.get_valid_entry(
            'Seu grafo é dirigido? (S/s para Sim, N/n para não): ',
            r"^[SsNn]{1}$"
        )
        is_directed = False if is_directed.lower() == 'n' else True

        # Quantidade de vértices
        vertexes_count = int(self.get_valid_entry(
            'Quantos vértices o seu grafo possui? ',
            r"^[0-9]+$"
        ))

        # Se deseja nomear os vértices
        give_a_name = self.get_valid_entry(
            'Deseja nomear seus vértices? (S/s para Sim, N/n para não): ',
            r"^[SsNn]{1}$"
        )
        give_a_name = False if give_a_name.lower() == 'n' else True

        # Nomeia os vértices
        if give_a_name:
            for vertex in range(vertexes_count):
                while True:
                    vertex_name = input(f'Digite um nome para o vértice {vertex + 1}: ')

                    if vertex_name not in self.vertexes:
                        break
                    else:
                        print('O grafo já possui uma vértice com esse nome')

                self.vertexes.append(vertex_name)
        # Numera os vértices
        else:
            self.vertexes = [
                str(vertex + 1) for vertex in range(vertexes_count)
            ]

        self.graph = Graph(is_directed)

    def validate_connections(self, vertex, connections):
        # Pega as conexões inválidas
        failed_connections = list(
            filter(lambda connection: (
                connection not in self.vertexes and connection not in [
                    '\n', '\t', '\r', ' ', ''
                ]
            ), connections
            )
        )

        """ Se todas as conexões forem válidas,
        adiciona as conexões ao vértice """
        if failed_connections == []:
            return True

        # Informa ao usuário que as conexões são inválidas
        else:
            vertexes_copy = self.vertexes.copy()
            vertexes_copy.remove(vertex)
            print(
                failed_connections,
                ' não são vértices válidos. Vértices válidos: ',
                vertexes_copy
            )
            return False

    def build_graph_input(self):
        # Adiciona os vértices ao grafo (chaves de um dicionário)
        for vertex in self.vertexes:
            self.graph.add_vertex(vertex)

        # Usuário insere as conexões de cada vértice
        for vertex in self.vertexes:
            while True:
                connections = input(
                    f"Digite as conexões do vértice '{vertex}' "
                    "separadas por vírgulas: "
                )
                # Converte a string em uma lista com cada conexão
                connections = connections.lower().replace(' ', '').split(',')

                # Verifica se os vértices da conexão são válidos
                are_valid = self.validate_connections(vertex, connections)

                if are_valid:
                    self.graph.add_connection(vertex, connections)
                    break

        print()

    # Grafos montados automaticamente
    def build_graph_auto(self, all_connections, is_directed, vertexes=[]):
        
        self.graph = Graph(is_directed)
        
        # Se foram passadas vértices, utiliza elas
        if vertexes != []:
            self.vertexes = vertexes
        # Caso contrário, numera os vértices pelo tamanho da lista de conexões
        else:
            self.vertexes = [
                str(vertex + 1) for vertex in range(len(all_connections))
            ]

        # Adiciona os vértices
        for vertex in self.vertexes:
            self.graph.add_vertex(vertex)

        count = 0
        # Adiciona as conexões nos vértices
        for vertex in self.vertexes:
            connections = all_connections[count]
            # Converte a string em uma lista com cada conexão
            connections = connections.lower().replace(' ', '').split(',')
            self.graph.add_connection(vertex, connections)
            
            count = count + 1
        
        print()

    def run_app(self):
        
        # Menu de interação com o usuário
        while True:
            case_num = input(
                "Digite: \n"
                " 1 : Para incluir um vértice\n"
                " 2 : Para incluir uma nova conexão\n"
                " 3 : Para excluir um vértice\n"
                " 4 : Para excluir uma conexão\n"
                " 5 : Para iniciar a busca em profundidade\n"
                " 6 : Para iniciar a busca em largura\n"
                " 7 : Para verificar se é conexo\n"
                " 8 : Para sair\n"
            )

            if case_num == "1":
                while True:
                    vertex_name = input(
                        "Digite a vértice que deseja incluir: "
                    )
                    if vertex_name not in self.vertexes:
                        break
                    else:
                        print('O grafo já possui uma vértice com esse nome')
                self.graph.add_vertex(vertex_name)
                self.vertexes.append(vertex_name)

                while True:
                    connection = input(
                        f"Digite as conexões do vértice '{vertex_name}' "
                        "separadas por vírgulas: "
                    )

                    # Converte a string em uma lista com cada conexão
                    connection = connection.lower().replace(' ', '').split(',')
                    are_valid = self.validate_connections(vertex_name, connection)

                    if are_valid:
                        self.graph.add_connection(vertex_name, connection)
                        self.graph.generate_matrix()
                        self.graph.print_matrix()
                        break

            elif case_num == "2":
                while True:
                    vertex_name = input(
                        "Digite o nome da vértice que deseja incluir uma conexão: "
                    )
                    if vertex_name in self.vertexes:
                        break
                    else:
                        print('O grafo não possui uma vértice com esse nome')

                while True:
                    connection = input(
                        f"Digite as novas conexões do vértice '{vertex_name}' "
                        "separadas por vírgulas: "
                    )

                    # Converte a string em uma lista com cada conexão
                    connection = connection.lower().replace(' ', '').split(',')
                    are_valid = self.validate_connections(vertex_name, connection)

                    if are_valid:
                        self.graph.add_connection(vertex_name, connection)
                        self.graph.generate_matrix()
                        self.graph.print_matrix()
                        break

            elif case_num == "3":
                while True:
                    vertex_name = input(
                        "Digite o nome da vértice que deseja excluir: "
                    )
                    if vertex_name in self.vertexes:
                        break
                    else:
                        print('O grafo não possui uma vértice com esse nome')

                self.graph.remove_vertex(vertex_name)
                self.graph.generate_matrix()
                self.graph.print_matrix()

            elif case_num == "4":
                while True:
                    vertex_name = input(
                        "Digite o nome da vértice que deseja excluir conexões: "
                    )
                    if vertex_name in self.vertexes:
                        break
                    else:
                        print('O grafo não possui uma vértice com esse nome')

                while True:
                    connection = input(
                        f"Digite as conexões do vértice '{vertex_name}' "
                        "que deseja excluir, separadas por vírgulas: "
                    )

                    # Converte a string em uma lista com cada conexão
                    connection = connection.lower().replace(' ', '').split(',')
                    are_valid = self.validate_connections(vertex_name, connection)

                    if are_valid:
                        self.graph.remove_connection(vertex_name, connection)
                        self.graph.generate_matrix()
                        self.graph.print_matrix()
                        break

            elif case_num == "5":
                while True:
                    search_start = input(
                        "Digite por qual vértice deseja iniciar "
                        "a busca em profundidade: "
                    )
                    if search_start in self.vertexes:
                        break
                    else:
                        print('O grafo não possui uma vértice com esse nome')
                while True:
                    wanted = input(
                        "Digite um vértice de parada "
                        "(enter para gerar a busca completa): "
                    )
                    if wanted in self.vertexes or wanted =='':
                        break
                    else:
                        print('O grafo não possui uma vértice com esse nome')

                wanted = None if wanted == '' else wanted
                self.graph.DFS_search(search_start, wanted)

            elif case_num == "6":
                while True:
                    search_start = input(
                        "Digite por qual vértice deseja iniciar "
                        "a busca em largura: "
                    )
                    if search_start in self.vertexes:
                        break
                    else:
                        print('O grafo não possui uma vértice com esse nome')
                while True:
                    wanted = input(
                        "Digite um vértice de parada "
                        "(enter para gerar a busca completa): "
                    )
                    if wanted in self.vertexes or wanted == '':
                        break
                    else:
                        print('O grafo não possui uma vértice com esse nome')
                wanted = None if wanted == '' else wanted
                self.graph.BFS_search(search_start, wanted)

            elif case_num == "7":
                location = input('Digite o vértice pelo qual deseja verificar a conectividade: ')
                while location not in self.graph.graph.keys():
                    print('Valor inválido, insira novamente')
                    location = input('Digite o vértice pelo qual deseja verificar a conectividade: ')
                
                self.graph.is_connected(location)

            elif case_num == "8":
                break
            else:
                print('Valor inválido, digite novamente')
