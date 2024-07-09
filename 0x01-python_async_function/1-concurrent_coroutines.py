#!/usr/bin/env python3
""" Multiple Coroutines Module """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Multiple coroutines at the same time with async

    Args:
        n (int): number of times to call wait_random
        max_delay (int): random value for the delay

    Returns:
        List: list of the delays
    """
    tasks = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]
    completed, _ = await asyncio.wait(tasks)

    list_delays = []
    for task in completed:
        list_delays.append(task.result())
    return list_delays
