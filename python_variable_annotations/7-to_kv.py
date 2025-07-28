#!/usr/bin/env python3

from typing import Tuple


def to_kv(k: str, v: float | int) -> Tuple[str, float]:
    """Function to return a tuple with the string k and the square of v as a float."""
    return (k, float(v*v)) 
