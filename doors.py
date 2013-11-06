#!/bin/python
import sys
import unittest

def doors(state):
    for i in range(1,len(state)+1):
        for j in range(i-1, len(state), i):
            state[j] = not state[j]
    return state
            

class TestDoors(unittest.TestCase):
    def test_doors(self):
        init_state = [True,True,True,True,True]
        result = doors(init_state)
        what_i_expect = [False,True,True,False,True]
        self.assertEquals(result, what_i_expect)

unittest.main()
