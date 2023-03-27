def possibility_of_rent(order_list: list[tuple]) -> bool:
    """
    Функция, которая находит пересечения по часам сдачи в аренду ракеты и определяющая хватит ли одной ракеты,
    чтобы удовлетворить все заявки на этот день.
    :param order_list: Список заявок на аренду ракеты в виде: [(час_начала, час_конца), (час_начала, час_конца)].
    :return: Ответ в виде True или False относительно того хватит ли одной ракеты для всех заявок или нет.
    """
    list_ = sorted(order_list, key=lambda x: x[0])

    for i in range(len(list_) - 1):
        if list_[i + 1][0] < list_[i][1]:
            return False
    return True


if __name__ == "__main__":
    print(possibility_of_rent([(1, 2), (2, 5), (1.5, 6)]))

    assert (possibility_of_rent([(1, 2), (2, 3)]) is True)
