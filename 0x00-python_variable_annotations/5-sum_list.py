#!/usr/bin/env python3
from typing import List
" Complex types - list of floats "


def sum_list(*input_list: List[float]) -> float:
    """
    Args:
        input_list: list of float
    Return:
        Sum of the list
    """
    return sum(*input_list)
