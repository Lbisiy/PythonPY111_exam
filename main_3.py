from collections import deque
import networkx as nx


def number_of_subgraph(graph_: nx.Graph) -> int:
    """
    Функция, считающая компонент связности графа.
    Если в графе есть несвязные подграфы, то функция выдает их кол-во.
    :param graph_: Граф.
    :return: Кол-во несвязных подграфов в графе.
    """
    number = nx.number_connected_components(graph_)
    return number


def number_of_subgraph2(graph_: nx.Graph) -> int:
    """
    Функция, считающая компонент связности графа.
    Если в графе есть несвязные подграфы, то функция выдает их кол-во
    :param graph_: Граф
    :return: Кол-во несвязных подграфов в графе
    """
    count = 0
    queue = deque()
    visited = {node: False for node in graph_}

    for node in graph_.nodes:
        if not visited[node]:
            queue.append(node)
            visited[node] = True
            count += 1

        while queue:
            current_node = queue.popleft()
            for nod in graph.neighbors(current_node):
                if not visited[nod]:
                    visited[nod] = True
                    queue.append(nod)
        continue
    return count


if __name__ == "__main__":
    graph = nx.Graph()
    graph.add_edges_from([
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('E', 'E'),
        ('F', 'G')
    ])
    print(number_of_subgraph(graph))
    print(number_of_subgraph2(graph))

    graph_2 = nx.Graph()
    graph_2.add_edges_from([
        ('A', 'A'), ('B', 'B')
    ])

    assert (number_of_subgraph(graph_2) == 2)
