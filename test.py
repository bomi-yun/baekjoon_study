﻿#-*- coding: utf-8 -*-
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
import sys

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
<<<<<<< Updated upstream

    
    def getStack(self):
        return self.stack
    
input = sys.stdin.readline().rstrip()
stack = Stack()
sum = 0

for s in input :
    if s == ')' and stack.top() == '(':
        stack.pop()
        stack.push(2)
    elif s == ']' and stack.top() == '[':
        stack.pop()
        stack.push(3)
    else :
        stack.push(s)

    if stack.top() == ')' :
        stack.pop()
        ret = stack.pop() * 2
        if not isinstance(ret,int) or stack.isEmpty(): break
        stack.pop()
        stack.push(ret)
    elif stack.top() == ']' :
        stack.pop()
        ret = stack.pop() * 3
        if not isinstance(ret,int) or stack.isEmpty(): break
        stack.pop()
        stack.push(ret)
        


    if not stack.isEmpty() and stack.top() != '(' and stack.top() != '[' and stack.top() != ')' and stack.top() != ']':
        
        tmp = stack.pop()
        
        if not stack.isEmpty() and stack.top() != '(' and stack.top() != '[' and stack.top() != ')' and stack.top() != ']':
            stack.push(stack.pop() + tmp)
        else:
            stack.push(tmp)
print(stack.getStack())
if stack.getSize() != 1 or (stack.top() == '[' or stack.top() == '('):
    print("0")
else :
    print(stack.top())
=======
case = int(sys.stdin.readline().rstrip())
stack = Stack()
for i in range(0, case):
    line = sys.stdin.readline().rstrip().split(' ')
    input = line[0]
    if input == 'pop':
        print(stack.pop())
    elif input == 'push':
        stack.push(int(line[1]))
    elif input == 'empty':
        if stack.isEmpty():
            print(1)
        else : print(0)
    elif input == 'top':
        print(stack.top())
    elif input == 'size':
        print(stack.getSize())
>>>>>>> Stashed changes
