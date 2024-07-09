#!/usr/bin/env python3
""" Measure the Runtime Module """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): number of times to call wait_random
        max_delay (int): random value for the delay

    Returns:
        float: total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
