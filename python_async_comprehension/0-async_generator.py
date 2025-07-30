#!/usr/bin/env python3
"""0. Async Generator"""

import asyncio
import random


async def async_generator():
    """Write a coroutine called async_generator that takes no arguments."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.randint(0, 10))
