#-*- coding: utf-8 -*-

class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.isEmpty():
            return -1
        else :
            ret = self.stack[len(self.stack)-1]
            del self.stack[len(self.stack)-1]
            return ret
        
    def push(self, data):
        self.stack.append(data)

    def getSize(self):
        return len(self.stack)

    def isEmpty(self):
        if len(self.stack) < 1: 
            return True
        else :
            return False

    def top(self):
        if not self.isEmpty():
            return self.stack[len(self.stack)-1]
        else:
            return -1
