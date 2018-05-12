#-*- coding: utf-8 -*-

import json
import sys
import Step_Question

class B_Week_3(Step_Question.Step):
    
    # https://www.acmicpc.net/step/5
    # https://www.acmicpc.net/step/6

    def __init__(self):
        self.step = Step_Question.Step()
        self.initList()

    def initList(self):
        self.step.addList('1152', self.L1152)
        self.step.addList('2577', self.L2577)
        self.step.addList('8958', self.L8958)
        self.step.addList('2920', self.L2920)
        self.step.addList('10039', self.L10039)

    
    def L1152(self):
        input = raw_input()
        input = input.strip()
        print(input.count(' ') + 1)

    def L2577(self):
        a = int(raw_input()) * int(raw_input()) * int(raw_input())
        n = [0]*10
        while a > 0 :
            n[a%10] += 1
            a /= 10
        
        for i in n:
            print(i)
            
    def L8958(self):
        case = int(raw_input())
        for d in range(0, case):
            input = raw_input()
            sum = 0
            b = 0
            for i in range(0, len(input)):
                if input[i] == 'O':
                    b += 1
                    sum += b
                else:
                    b = 0
            print(sum)

    def L2920(self):
        # import sys
        input = sys.stdin.readline().rstrip()
        list = input.split(' ')
        ret = ""
        for i in range(1, len(list)):
            if list[i] > list[i-1] and (ret == "" or ret == "ascending"):
                ret = "ascending"
            elif list[i] < list[i-1] and (ret == "" or ret == "descending"): 
                ret = "descending"
            else:
                ret = "mixed"
                break
        print(ret)

    def L10039(self):
        # import sys
        sum = 0
        for i in range(0, 5):
            input = int(sys.stdin.readline().rstrip())
            if input < 40 : sum += 40
            else: sum += input
        print(str(sum/5))
    