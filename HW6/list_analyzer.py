"""
Module: list_analyzer.py

This module defines the ListAnalyzer class, which can analyze two lists of numbers
and compare their average values.
"""


class ListAnalyzer:
    """
    A class to analyze two lists of numbers and compare their average values.
    """

    def __init__(self, list1, list2):
        """
        Initialize the ListAnalyzer with two lists of numbers.

        Args:
            list1 (list): The first list of numbers.
            list2 (list): The second list of numbers.
        """
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        """
        Calculate the average of a list of numbers.

        Args:
            lst (list): The list of numbers.

        Returns:
            float: The average value of the list.
        """
        if not lst:
            return 0
        for item in lst:
            if not isinstance(item, (int, float)):
                raise TypeError("Invalid input. Please enter valid numbers separated by spaces.")
        return sum(lst) / len(lst)

    def compare_averages(self):
        """
        Compare the average values of the two lists.

        Returns:
            str: A message indicating which list has a larger average value.
        """
        try:
            avg1 = self.calculate_average(self.list1)
            avg2 = self.calculate_average(self.list2)

            if avg1 > avg2:
                return "The first list has a larger average value"
            elif avg2 > avg1:
                return "The second list has a larger average value"
            else:
                return "Average values are equal"
        except ValueError as exc:
            return str(exc)


if __name__ == "__main__":
    try:
        list1 = [float(x) for x in input("Enter the first list "
                                         "of numbers separated by spaces: ").split()]
        list2 = [float(x) for x in input("Enter the second list "
                                         "of numbers separated by spaces: ").split()]

        analyzer = ListAnalyzer(list1, list2)
        result = analyzer.compare_averages()

        print(result)
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")
