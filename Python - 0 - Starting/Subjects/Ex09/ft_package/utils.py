"""
Utility functions for ft_package.

This module provides functions to perform operations on lists.
"""

from typing import List, Any


def count_in_list(items: List[Any], target: Any) -> int:
    """
    Count the number of occurrences of a target element in a list.

    Args:
        items (List[Any]): The list to search.
        target (Any): The element to count.

    Returns:
        int: The number of times the target appears in the list.
    """
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count


def reverse_list(items: List[Any]) -> List[Any]:
    """
    Reverse the order of elements in a list.

    Args:
        items (List[Any]): The list to reverse.

    Returns:
        List[Any]: A new list with elements in reverse order.
    """
    reversed_items = []
    for item in items:
        reversed_items.insert(0, item)
    return reversed_items