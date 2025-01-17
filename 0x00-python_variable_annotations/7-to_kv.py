#!/usr/bin/env python3
" Complex types - string and int/float to tuple "
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k: str
        v: int || float
    Return:
        Tuple(k, v**2)
    """
    return (k, v**2)
