#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """ write an async routine called wait_n that takes in 2 int arguments"""

    task = []

    for _ in range(n):

        task.append(task_wait_random(max_delay))

    delais = await asyncio.gather(*task)

    a = len(delais)
    for i in range(a):
        for j in range(0, a-i-1):
            if delais[j] > delais[j+1]:
                delais[j], delais[j+1] = delais[j+1], delais[j]
    return delais
