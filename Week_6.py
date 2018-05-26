#-*- coding: utf-8 -*-

import json
import sys
import Step_Question

class B_Week_6(Step_Question.Step):
    # 완료
    # https://www.acmicpc.net/step/9

    def __init__(self, step):
        self.step = step
        self.initList()

    def initList(self):
        self.step.addList('2750', self.L2750)

    def L2750(self): #선택정렬
        #import sys
        case = int(sys.stdin.readline().rstrip())
        l = [int(sys.stdin.readline().rstrip()) for col in range(case)]
        
        tmp = 0
        cur = 0
        for i in range(0, len(l)-1):
            min = 10000
            cur = 0
            for j in range(i, len(l)):
                if l[j] < min : 
                    min = l[j]
                    cur = j
                    # break
            if i != cur: #swqp
                tmp = l[cur]
                l[cur] = l[i]
                l[i] = tmp
            print(str(l[i]))
        print(str(l[len(l)-1]))

    def L2751(self):
        c = 0
        l = [5, 3, 1, 2, 4]
        while len(l) > 2**c:
            c += 1