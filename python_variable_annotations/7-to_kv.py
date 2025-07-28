#!/usr/bin/env python3

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function to return a tuple"""
    return (k, (v ** 2))
