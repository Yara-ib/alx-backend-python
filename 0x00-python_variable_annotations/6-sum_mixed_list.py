#!/usr/bin/env python3
" Complex types - mixed list "
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_lst: list of float & int
    Return:
        Sum of the list
    """
    return sum(mxd_lst)
