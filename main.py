import sys
import networkx as nx
import matplotlib.pyplot as plt
from typing import List

NO_PARENT = -1


def dijkstra(adjacency_matrix: List[List[int]], start_vertex: int):
    n_vertices = len(adjacency_matrix[0])

    shortest_distances = [sys.maxsize] * n_vertices
    added = [False] * n_vertices

    shortest_distances[start_vertex] = 0

    parents = [NO_PARENT] * n_vertices

    # nearest_vertex e shortest_distance são inicializados para representar o vértice mais próximo que ainda não foi visitado
    # e a distância mais curta para vértice
    for _ in range(1, n_vertices):
        nearest_vertex = -1
        shortest_distance = sys.maxsize
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]

        added[nearest_vertex] = True

        for vertex_index in range(n_vertices):
            edge_distance = adjacency_matrix[nearest_vertex][vertex_index]

            if edge_distance > 0 and ((shortest_distance + edge_distance) < shortest_distances[vertex_index]):
                parents[vertex_index] = nearest_vertex
                shortest_distances[vertex_index] = shortest_distance + edge_distance

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
