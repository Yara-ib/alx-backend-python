#!/usr/bin/env python3
""" Multiple Tasks Module """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Multiple tasks at the same time with async

    Args:
        n (int): number of times to call wait_random
        max_delay (int): random value for the delay

    Returns:
        List: list of the delays
    """
    tasks = [
       task_wait_random(max_delay) for _ in range(n)
    ]
    completed, _ = await asyncio.wait(tasks)

    list_delays = []
    for task in completed:
        list_delays.append(task.result())
    return sorted(list_delays)
