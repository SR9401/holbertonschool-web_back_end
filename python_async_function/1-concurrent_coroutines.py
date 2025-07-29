#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ write an async routine called wait_n that takes in 2 int arguments"""

    task = []

    for _ in range(n):

        task.append(wait_random(max_delay))

    delais = await asyncio.gather(*task)

    return sorted(delais)
