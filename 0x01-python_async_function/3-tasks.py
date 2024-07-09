#!/usr/bin/env python3
""" Creating Tasks """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> type:
    """
    Regular function takes an integer as a max_delay to act like async function

    Args:
        max_delay (int): value for the delay

    Returns:
        type: <class '_asyncio.Task'>
    """
    return asyncio.create_task(wait_random(max_delay))
