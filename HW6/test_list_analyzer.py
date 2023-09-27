"""
Модуль: test_list_analyzer.py

Данный модуль содержит модульные тесты для класса ListAnalyzer в файле list_analyzer.py.
"""
import pytest
from list_analyzer import ListAnalyzer


# Тестовый пример для сценария, в котором первый список имеет большее среднее значение.
def test_first_list_has_larger_average():
    """
    Протестируйте сценарий, в котором первый список имеет большее среднее значение.
    """
    list1 = [1, 2, 3]
    list2 = [1, 2, 2]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Первый список имеет большее среднее значение"


# Тестовый пример для сценария, когда второй список имеет большее среднее значение.
def test_second_list_has_larger_average():
    """
    Протестируйте сценарий, в котором второй список имеет большее среднее значение.
    """
    list1 = [1, 2, 2]
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Второй список имеет большее среднее значение"


# Тестовый пример для сценария, в котором средние значения равны.
def test_average_values_are_equal():
    """
    Тест для сценария, когда средние значения обоих списков равны.
    """
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Средние значения равны"


# Тестовый пример для сценария, когда один из списков пуст.
def test_one_empty_list():
    """
    Тест для сценария, когда один из списков пуст.
    """
    list1 = []
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Второй список имеет большее среднее значение"


# Тестовый пример для сценария, когда оба списка пусты.
def test_both_empty_lists():
    """
    Тест для сценария, когда оба списка пусты.
    """
    list1 = []
    list2 = []
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Средние значения равны"


# Тестовый пример для некорректного ввода (нечисловые значения в списках).
def test_invalid_input():
    """
    Проверка на некорректный ввод с нечисловыми значениями в списках.
    """
    list1 = [1, 2, "a"]
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    with pytest.raises(TypeError) as exc_info:
        analyzer.compare_averages()
    assert "Неверный ввод. Пожалуйста, введите правильные числа, " \
           "разделенные пробелами." in str(exc_info.value)


# Тестовый пример для сценария, в котором один список пуст, а другой имеет значения.
def test_one_list_empty():
    """
    Тест для сценария, когда один список пуст, а другой имеет значения.
    """
    list1 = []
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Второй список имеет большее среднее значение"


# Тестовый пример для сценария, когда оба списка имеют одно и то же единственное значение.
def test_single_value_lists():
    """
    Тест для сценария, когда оба списка имеют одно и то же единственное значение.
    """
    list1 = [3]
    list2 = [3]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Средние значения равны"


# Тестовый пример для сценария, когда один список имеет единственное значение, а другой пуст.
def test_single_value_and_empty_list():
    """
    Тест для сценария, когда один список имеет единственное значение, а другой пуст.
    """
    list1 = [3]
    list2 = []
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Первый список имеет большее среднее значение"


# Тестовый пример для некорректного ввода (один список пуст, а другой имеет нечисловые значения).
def test_empty_and_invalid_input():
    """
    Тест на сценарий, в котором один список пуст, а другой имеет нечисловые значения.
    """
    list1 = []
    list2 = [1, "a", 3]
    analyzer = ListAnalyzer(list1, list2)
    with pytest.raises(TypeError) as exc_info:
        analyzer.compare_averages()
    assert "Неверный ввод. Пожалуйста, введите правильные числа, разделенные пробелами." in str(exc_info.value)


# Тестовый пример для недопустимого ввода (оба списка содержат нечисловые значения).
def test_both_lists_invalid_input():
    """
    Тест на сценарий, когда оба списка содержат нечисловые значения.
    """
    list1 = ["a", "b", "c"]
    list2 = ["x", "y", "z"]
    analyzer = ListAnalyzer(list1, list2)
    with pytest.raises(TypeError) as exc_info:
        analyzer.compare_averages()
    assert "Неверный ввод. Пожалуйста, введите правильные числа, разделенные пробелами." in str(exc_info.value)


if __name__ == "__main__":
    pytest.main()
