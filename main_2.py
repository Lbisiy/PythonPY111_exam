def counter(n, k) -> int:
    """
    Функция, реализующая считалочку. Считалка начинает считать с первого человека.
    Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
    :param n: Кол-во человек.
    :param k: Кол-во слогов в считалочке.
    :return: Номер последнего оставшегося человека.
    """
    list_ = [num for num in range(1, n + 1)]

    while len(list_) != 1:
        if k > len(list_):
            ind_ = (k - 1) % len(list_)
        else:
            ind_ = k - 1
        list_.pop(ind_)

    return list_[-1]


if __name__ == "__main__":
    a = counter(20, 7)
    print(a)

    assert (counter(2, 3) == 2)
