#-*- coding: utf-8 -*-

import json
import sys
import Step_Question

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
    
    def getStack(self):
        return self.stack

class B_Week_8(Step_Question.Step):
    # 완료
    # https://www.acmicpc.net/step/11

    def __init__(self, step):
        self.step = step
        self.initList()

    def initList(self):
        self.step.addList('10828', self.L10828)
        self.step.addList('1874', self.L1874)
        self.step.addList('9012', self.L9012)
        self.step.addList('2504', self.L2504)

    def L10828(self):
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


    #top보다 input의 값이 작으면 NO??

    def L1874(self):
        case = int(sys.stdin.readline().rstrip())
        stack = Stack()
        result = ""
        data = 1
        flag = True
        for i in range(0, case):
            input = int(sys.stdin.readline().rstrip())
            while stack.top() != input :
                stack.push(data)
                result += "+\n"
                data += 1
                if not stack.isEmpty() and stack.top() > input:
                    result = "NO"
                    flag = False
                    break
            if flag : 
                stack.pop()
                result += "-\n"
        print(result)
    
    def L9012(self):
        case = int(sys.stdin.readline().rstrip())
        for i in range(0, case):
            stack = Stack()
            input = sys.stdin.readline().rstrip()
            for s in input :
                if stack.isEmpty() and s == ")":
                    stack.push(s)
                    break    
                elif not stack.isEmpty() and stack.top() != s :
                    stack.pop()
                else :
                    stack.push(s)
                    
            if stack.getSize() > 0 :
                print("NO")
            else :
                print("YES")

    def L2504(self): #틀렸음
        input = sys.stdin.readline().rstrip()
        stack = Stack()
        n = Stack()
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
                    
        if stack.getSize() != 1 or (stack.top() == '[' or stack.top() == '('):
            print("0")
        else :
            print(stack.top())