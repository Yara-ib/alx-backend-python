#!/usr/bin/env python3
""" Parallel Comprehensions Module """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that execute async_comprehension 4 times
    in parallel using asyncio.gather

    Returns:
        float: The total runtime
    """
    start = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.perf_counter()
    return end - start
