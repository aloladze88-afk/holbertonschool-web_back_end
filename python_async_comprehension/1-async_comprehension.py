#!/usr/bin/env python3
"""Module for collecting values from an async generator."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return 10 random numbers collected from async_generator."""
    return [number async for number in async_generator()]
