#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to return a tuple"""
    return (k, (v ** 2))
