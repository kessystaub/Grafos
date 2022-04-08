from App import App

app = App()

# ===========================================
# INPUT DO USUÁRIO:

# app.user_graph_config()
# app.build_graph_input()
7
7
# ===========================================
# AUTOMÁTICO:

#SEPARADOS:
# app.build_graph_auto(
#     all_connections=[
#         'e,f,g,i',
#         'g',
#         'h',
#         'h',
#         'a,f,i',
#         'a,e,i',
#         'a,b',
#         'c,d',
#         'a,e,f'
#     ],
#     is_directed=False,
#     vertexes=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# )

# -------------------------------------------

# NÃO-DIRIGIDO:
# app.build_graph_auto(
#     all_connections=[
#         '2,4,6',
#         '1,3,4,5',
#         '2,4,5,6',
#         '1,2,3',
#         '2,3,6',
#         '1,3,5'
#     ],
#     is_directed=False,
# )

# -------------------------------------------

# DIRIGIDO
# app.build_graph_auto(
#     all_connections=[
#         '2,6',
#         '3,4',
#         '5,6',
#         '1,3',
#         '2',
#         '5'
#     ],
#     is_directed=True,
# )

# DESCONEXO COM 2 SUB-GRAFOS
# app.build_graph_auto(
#     all_connections=[
#         'd,b',
#         'c',
#         'g',
#         'e,f',
#         'a,g,c,b',
#         'c',
#         'f,b'
#     ],
#     is_directed=True,
#     vertexes=['a', 'b', 'c', 'd', 'e', 'f','g']
# )

# DESCONEXO COM 3 SUB-GRAFOS COM ERRO
# app.build_graph_auto(
#     all_connections=[
#         'd,b',
#         'c',
#         'g',
#         'e,f',
#         'a,g,c,b',
#         'c',
#         'f,b',
#         'f,j',
#         'k',
#         'i'
#     ],
#     is_directed=True,
#     vertexes=['a', 'b', 'c', 'd', 'e', 'f','g','i','j','k']
# )


# DESCONEXO COM 3 SUB-GRAFOS TALVEZ COM ERRO
# app.build_graph_auto(
#     all_connections=[
#         'd,b',
#         'c',
#         'g',
#         'e,f',
#         'a,g,c,b',
#         'c',
#         'f,b',
#         'f,j',
#         'k,c',
#         'i,d'
#     ],
#     is_directed=True,
#     vertexes=['a', 'b', 'c', 'd', 'e', 'f','g','i','j','k']
# )

# CONEXO
app.build_graph_auto(
    all_connections=[
        'c',
        'g',
        'f,b',
        'c',
    ],
    is_directed=True,
    vertexes=['b', 'c', 'g','f']
)


# ===========================================

app.graph.generate_matrix()
app.graph.print_matrix()
app.run_app()
