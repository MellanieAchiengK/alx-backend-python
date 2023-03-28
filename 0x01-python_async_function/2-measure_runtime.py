#!/usr/bin/env python3
"""
Module that measures the execution time for wait_n function
"""

import asyncio
from time import perf_counter
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_delay(n: int, max_delay: int) -> List[float]:
    """Measures the total delay for n executions of wait_random"""
    start_time = perf_counter()
    await wait_n(n, max_delay)
    end_time = perf_counter()

    return end_time - start_time


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measures the total execution time for n calls of wait_n"""
    asyncio.run(measure_delay(n, max_delay))
    total_time = asyncio.run(measure_delay(n, max_delay))
    return total_time / n
