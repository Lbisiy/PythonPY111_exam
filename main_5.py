import networkx as nx


def navigator(array: list[list], start, finish) -> list:
    """
    Функция-навигатор, которая на основании двумерного массива с указанными весами входа на каждую ячейку,
    определяет путь с минимальной стоимостью из ячейки start до ячейки finish.
    :param array: Двумерный массив с весами.
    :param start: Координаты ячейки старта.
    :param finish: Координаты ячейки финиша.
    :return: Минимальная стоимость пути.
    """
    rows = len(array)
    cols = len(array[0])
    graph = nx.DiGraph()
    list_ = []

    for x in range(rows):
        for y in range(cols):
            neighbors = [(x - 1, y),
                         (x + 1, y),
                         (x, y - 1),
                         (x, y + 1),
                         (x - 1, y + 1),
                         (x - 1, y - 1),
                         (x + 1, y + 1),
                         (x + 1, y - 1)]
            for i, j in neighbors:
                if 0 <= i < rows and 0 <= j < cols:
                    list_.append(((x, y), (i, j), array[i][j]))

    graph.add_weighted_edges_from(list_)
    path = nx.dijkstra_path_length(graph, start, finish)
    return path


if __name__ == "__main__":
    array_ = [
        [4, 8, 7],
        [5, 2, 1],
        [6, 15, 3]
    ]
    print(navigator(array_, (0, 0), (2, 2)))

    assert (navigator([[3, 5]], (0, 0), (0, 1)) == 5)
