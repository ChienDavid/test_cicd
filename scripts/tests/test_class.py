#!/usr/bin/env python3



class TestClass:
    def test_one(self):
        x = 'hello'
        assert 'h' in x

    def test_two(self):
        x = TestClass
        assert hasattr(x, 'test_one')
