#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """write a measure_runtime coroutine that will execute async_comprehension"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()

    exec_time = end_time - start_time
    return exec_time
