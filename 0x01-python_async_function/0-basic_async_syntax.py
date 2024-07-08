#!/usr/bin/env python3
""" Basics of Async Module """
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine waits for a random delay between 0 & max_delay

    Args:
        max_delay (int, optional): Random value | Defaults to 10.

    Returns:
        float: value of the random delay
    """
    max_delay = uniform(0, 10)
    await sleep(max_delay)
    return max_delay
