#!/usr/bin/env python3
""" Async Comprehensions Module """
import asyncio
import random
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    Coroutine collect 10 random numbers using an async comprehension
    over async_generator, then return the 10 random numbers

    Returns:
        Generator[float, None, None]: The value of the delays

    Yields:
        Iterator[Generator[float, None, None]]: Yields random delays in a list
    """
    return [i async for i in async_generator()]
