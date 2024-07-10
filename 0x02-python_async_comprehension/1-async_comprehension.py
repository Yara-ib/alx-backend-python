#!/usr/bin/env python3
""" Async Comprehensions Module """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine collect 10 random numbers using an async comprehension
    over async_generator, then return the 10 random numbers

    Returns:
        List[float]: The list of 10 random numbers
    """
    return [i async for i in async_generator()]
