#!/usr/bin/env python3
""" Type Annotations """
from typing import Mapping, Union, Any, TypeVar


T = TypeVar('T')
Un = Union[Any, T]
All = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: All = None) -> Un:
    """ More Type Annotations """
    if key in dct:
        return dct[key]
    else:
        return default
