#!/usr/bin/env python3
""" Complex types - Functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function multiplies a float by multiplier """
    def fn(x: float) -> float:
        """ Multiplies a float by multiplier from the main function """
        return x * multiplier
    return fn
