#!/usr/bin/env python3

def increase(x):
    return x + 1

def decrease(x):
    return x - 1

def test_increase():
    assert increase(4) == 5

def test_decrease():
    assert decrease(4) == 3


