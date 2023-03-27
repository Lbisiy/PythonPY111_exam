def consensus_string(list_of_str: list[str]) -> str:
    """
    Функция, создающая консенсус-строку на основании списка из N строк.
    Читает строки, определяет наиболее встречающиеся символы в каждом месте строк и на основании этого строит
    консенсус-строку, в которой на каждом месте будет.
    стоять тот символ, который чаще всего встречался в этом месте суммарно во всех чтениях.
    :param list_of_str: Список строк одинаковой длины.
    :return: Консенсус-строка.
    """

    length_ = len(list_of_str[0])
    symbol_dict = {i: {} for i in range(length_)}
    string = ''

    for str_ in list_of_str:
        for i, _ in enumerate(str_):
            if symbol_dict[i].get(str_[i]) is not None:
                symbol_dict[i][str_[i]] += 1
            else:
                symbol_dict[i][str_[i]] = 1

    for key, dict_ in symbol_dict.items():
        symbol_dict[key] = dict(sorted(dict_.items(), key=lambda x: (-x[1], x[0])))
        key = list(symbol_dict[key].keys())
        string += key[0]
    return string


if __name__ == "__main__":
    print(consensus_string(['ATTA', 'ACTA', 'AGCA', 'ACAA']))

    assert (consensus_string(['ATTA', 'ATTA', 'ATTA', 'CCCC']) == 'ATTA')
