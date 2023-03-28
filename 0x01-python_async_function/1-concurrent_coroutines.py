#!/usr/bin/env python3
""" wait_random """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ takes in 2 int arguments and return the list
        of all the delays (float values) """
    delays = []
    # Create a list of coroutines to be executed concurrently
    coroutines = [wait_random(max_delay) for i in range(n)]
    # Wait for all coroutines to finish execution
    for task in asyncio.as_completed(coroutines):
        delay = await task
        delays.append(delay)
    return delays
