#!/usr/bin/env python3
""" Async Generator Module """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async Generator will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10

    Returns:
        Generator[float, None, None]: The value of the delays

    Yields:
        Iterator[Generator[float, None, None]]: Yields random delays in a list
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
