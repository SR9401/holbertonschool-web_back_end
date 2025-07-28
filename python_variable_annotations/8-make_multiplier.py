#!/usr/bin/env python3
"""8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multipliate"""
    def multiplier_function(x: float) -> float:
        """function that multipliate"""
        return x * multiplier
    return multiplier_function
