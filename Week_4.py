#-*- coding: utf-8 -*-

import json
import sys
import Step_Question

class B_Week_4(Step_Question.Step):
    
    # https://www.acmicpc.net/step/5
    # https://www.acmicpc.net/step/6

    def __init__(self, step):
        self.step = step
        self.initList()

    def initList(self):
        self.step.addList('1152', self.L1152)
        self.step.addList('2577', self.L2577)
        self.step.addList('8958', self.L8958)
        self.step.addList('2920', self.L2920)
        self.step.addList('10039', self.L10039)
        self.step.addList('11654', self.L11654)
        self.step.addList('10809', self.L10809)
        self.step.addList('2675', self.L2675)
        self.step.addList('1157', self.L1157)
        self.step.addList('2908', self.L2908)
        self.step.addList('5622', self.L5622)
        self.step.addList('2941', self.L2941)

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
    
    def L11654(self):
        # import sys
        print(ord(sys.stdin.readline().rstrip()))


    def L10809(self):
        # import sys
        input = sys.stdin.readline().rstrip()
        for i in range(ord('a'), ord('z')+1):
            print(input.find(chr(i))),

    def L2675(self):
        #import sys
        case = int(sys.stdin.readline().rstrip())
        for j in range(0, case):
            input = sys.stdin.readline().rstrip()
            for i in range(2, len(input)):
                sys.stdout.write(input[i]*int(input[0]))
            print('')

    def L1157(self): #시간초과 sort때문인듯...
        #import sys
        input = sys.stdin.readline().rstrip().upper()
        max = ''
        list = [0]*len(input)
        for i in range(0, len(input)):
            c = input.count(input[i])
            list[i] = c
            if max == '':
                max = input[i]
            elif max != '' and input.count(max) < c:
                max = input[i]
        list.sort()
        if len(input) > 2 and list[0] == list[1] : sys.stdout.write('?')
        else : sys.stdout.write(max)

    def L2908(self):
        #import sys
        input = sys.stdin.readline().rstrip().split(' ')
        input[0] = int(input[0])
        input[1] = int(input[1])
        for j in range(0, len(input)):
            tmp = input[j]
            input[j] = 0
            while tmp > 0:
                input[j] *= 10
                input[j] += tmp % 10
                tmp /= 10
        if input[0] > input[1] : sys.stdout.write(str(input[0]))
        else : sys.stdout.write(input[1])

    def L5622(self):
        #import sys
        input = sys.stdin.readline().rstrip()
        sum = 0
        for s in input:
            if s >= 'A' and s <= 'C':
                sum += 3
            elif s >= 'D' and s <= 'F':
                sum += 4 
            elif s >= 'G' and s <= 'I':
                sum += 5 
            elif s >= 'J' and s <= 'L':
                sum += 6 
            elif s >= 'M' and s <= 'O':
                sum += 7 
            elif s >= 'P' and s <= 'S':
                sum += 8 
            elif s >= 'T' and s <= 'V':
                sum += 9 
            else:
                sum += 10
        print(sum)

    def L2941(self):
        #import sys
        input = sys.stdin.readline().rstrip()
        list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
        count = 0
        while len(input) > 0:
            for s in list:
                if s == input[0:len(s)] :
                    # print(s)
                    # print(input[0:len(s)])
                    count += 1
                    input = input[len(s):len(input)]
                    print(input)
                    break
        print(count)