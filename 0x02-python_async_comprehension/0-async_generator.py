#!/usr/bin/env python3
""" Async Generator Module """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Async Generator will loop 10 times,
    each time asynchronously wait 1 second,
    then yield a random number between 0 and 10

    Returns:
        AsyncGenerator[int, None]: The value of the delays

    Yields:
        Iterator[AsyncGenerator[int, None]]: Yields the delay in a list
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
