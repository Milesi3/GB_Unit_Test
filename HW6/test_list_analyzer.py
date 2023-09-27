"""
Module: test_list_analyzer.py

This module contains unit tests for the ListAnalyzer class in list_analyzer.py.
"""
import pytest
from list_analyzer import ListAnalyzer


# Test case for the scenario where the first list has a larger average.
def test_first_list_has_larger_average():
    """
    Test for the scenario where the first list has a larger average value.
    """
    list1 = [1, 2, 3]
    list2 = [1, 2, 2]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "The first list has a larger average value"


# Test case for the scenario where the second list has a larger average.
def test_second_list_has_larger_average():
    """
    Test for the scenario where the second list has a larger average value.
    """
    list1 = [1, 2, 2]
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "The second list has a larger average value"


# Test case for the scenario where average values are equal.
def test_average_values_are_equal():
    """
    Test for the scenario where average values of both lists are equal.
    """
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Average values are equal"


# Test case for the scenario where one of the lists is empty.
def test_one_empty_list():
    """
    Test for the scenario where one of the lists is empty.
    """
    list1 = []
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "The second list has a larger average value"


# Test case for the scenario where both lists are empty.
def test_both_empty_lists():
    """
    Test for the scenario where both lists are empty.
    """
    list1 = []
    list2 = []
    analyzer = ListAnalyzer(list1, list2)
    assert analyzer.compare_averages() == "Average values are equal"


# Test case for invalid input (non-numeric values in the lists).
def test_invalid_input():
    """
    Test for invalid input with non-numeric values in the lists.
    """
    list1 = [1, 2, "a"]
    list2 = [1, 2, 3]
    analyzer = ListAnalyzer(list1, list2)
    with pytest.raises(TypeError) as exc_info:
        analyzer.compare_averages()
    assert "Invalid input. Please enter valid numbers separated by spaces." in str(exc_info.value)


if __name__ == "__main__":
    pytest.main()
