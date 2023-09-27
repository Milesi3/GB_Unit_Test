"""
Модуль: list_analyzer.py

Данный модуль определяет класс ListAnalyzer, который может анализировать два списка чисел
и сравнивать их средние значения.
"""


class ListAnalyzer:
    """
    Занятие по анализу двух списков чисел и сравнению их средних значений.
    """

    def __init__(self, list1, list2):
        """
        Инициализация ListAnalyzer двумя списками чисел.

        Args:
            list1 (список): Первый список чисел.
            list2 (список): Второй список чисел.
        """
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        """
        Вычислить среднее значение списка чисел.

        Args:
            lst (список): Список чисел.

        Returns:
            float: Среднее значение по списку.
        """
        if not lst:
            return 0
        for item in lst:
            if not isinstance(item, (int, float)):
                raise TypeError("Неверный ввод. Пожалуйста, введите правильные числа, "
                                "разделенные пробелами.")
        return sum(lst) / len(lst)

    def compare_averages(self):
        """
        Сравнить средние значения двух списков.

        Returns:
            str: Сообщение, указывающее, какой список имеет большее среднее значение.
        """
        try:
            avg1 = self.calculate_average(self.list1)
            avg2 = self.calculate_average(self.list2)

            if avg1 > avg2:
                return "Первый список имеет большее среднее значение"
            elif avg2 > avg1:
                return "Второй список имеет большее среднее значение"
            else:
                return "Средние значения равны"
        except ValueError as exc:
            return str(exc)


# if __name__ == "__main__":
#     try:
#         list1 = [float(x) for x in input("Введите первый список чисел, "
#                                          "разделенных пробелами: ").split()]
#         list2 = [float(x) for x in input("Введите второй список чисел, "
#                                          "разделенных пробелами: ").split()]
#
#         analyzer = ListAnalyzer(list1, list2)
#         result = analyzer.compare_averages()
#
#         print(result)
#     except ValueError:
#         print("Неверный ввод. Пожалуйста, введите правильные числа, разделенные пробелами.")
