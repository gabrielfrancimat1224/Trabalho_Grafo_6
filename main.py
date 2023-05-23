import sys
import networkx as nx
import matplotlib.pyplot as plt
from typing import List

NO_PARENT = -1


def dijkstra(adjacency_matrix: List[List[int]], start_vertex: int):
    n_vertices = len(adjacency_matrix[0])

    # Inicialização das distâncias mais curtas para cada vértice
    # Inicialmente, todas as distâncias são definidas como infinito (sys.maxsize)
    shortest_distances = [sys.maxsize] * n_vertices
    # Marcador para indicar se o vértice foi "adicionado"
    # Isto é, se a distância mais curta para este vértice já foi encontrada
    added = [False] * n_vertices

    # A distância do vértice inicial para si mesmo é sempre 0
    shortest_distances[start_vertex] = 0

    # Lista de pais (precedentes) para cada vértice
    # Para reconstruir o caminho mais curto de cada vértice ao vértice inicial
    parents = [NO_PARENT] * n_vertices

    # Loop para encontrar a distância mais curta para cada vértice
    for _ in range(1, n_vertices):
        # Inicialização do vértice mais próximo e da distância mais curta
        nearest_vertex = -1
        shortest_distance = sys.maxsize
        # Loop para encontrar o vértice não adicionado mais próximo
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]

        # Marca o vértice mais próximo como "adicionado"
        added[nearest_vertex] = True

        # Loop para atualizar as distâncias dos vértices adjacentes ao vértice mais próximo
        for vertex_index in range(n_vertices):
            edge_distance = adjacency_matrix[nearest_vertex][vertex_index]

            if edge_distance > 0 and ((shortest_distance + edge_distance) < shortest_distances[vertex_index]):
                parents[vertex_index] = nearest_vertex
                shortest_distances[vertex_index] = shortest_distance + edge_distance

    # Imprime a solução e desenha o gráfico
    print_solution(start_vertex, shortest_distances, parents)
    draw_graph(parents, start_vertex)


def print_solution(start_vertex: int, distances: List[int], parents: List[int]):
    n_vertices = len(distances)
    print("Árvore da distância mínima a partir do vértice: " + str(start_vertex))

    for vertex_index in range(n_vertices):
        if vertex_index != start_vertex:
            print("Caminho " + str(start_vertex) + " -> " + str(vertex_index) + ": ", end="")
            print_path(vertex_index, parents)
            print(" Distância: " + str(distances[vertex_index]))


def print_path(current_vertex: int, parents: List[int]):
    if current_vertex == NO_PARENT:
        return
    print_path(parents[current_vertex], parents)
    print(current_vertex, "-> ", end="")


def draw_graph(parents: List[int], start_vertex: int):
    G = nx.DiGraph()

    for i, parent in enumerate(parents):
        if parent != NO_PARENT:
            G.add_edge(parent, i)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()


def main():
    adjacency_matrix = [
        [0, 5, 7, 1, 0, 0, 0],
        [5, 0, 2, 3, 0, 0, 0],
        [7, 2, 0, 6, 5, 1, 0],
        [1, 3, 6, 0, 0, 5, 3],
        [0, 0, 5, 0, 0, 4, 1],
        [0, 0, 1, 5, 4, 0, 0],
        [0, 0, 0, 3, 1, 0, 0]
    ]

    adjacency_matrix2 = [
        {0, 0, 0, 0, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 11, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0},
        {0, 11, 0, 3, 0, 3, 5, 0, 0, 6, 0, 0, 0, 0},
        {0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 5},
        {5, 1, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0},
        {1, 0, 3, 0, 6, 0, 1, 0, 5, 7, 1, 0, 4, 0},
        {0, 0, 5, 4, 0, 1, 0, 0, 5, 7, 1, 0, 0, 0},
        {0, 0, 0, 0, 8, 0, 10, 0, 5, 7, 1, 0, 7, 0},
        {0, 0, 0, 0, 0, 6, 0, 10, 0, 0, 0, 0, 0, 0},
        {0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 13, 8, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 9, 6},
        {2, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 4, 0, 7, 0, 0, 9, 0, 0, 0},
        {0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0},
    ]

    start_vertex = int(input("Digite o vértice inicial: "))

    if 0 <= start_vertex < len(adjacency_matrix):
        dijkstra(adjacency_matrix, start_vertex)
    else:
        print("Vértice inválido. Deve ser entre 0 e " + str(len(adjacency_matrix) - 1))


if __name__ == "__main__":
    main()
