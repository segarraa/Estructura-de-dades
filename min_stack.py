# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:59:57 2026

@author: Usuario
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.mins  = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.mins:
            self.mins.append(min(val, self.mins[-1]))
        else:
            self.mins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]