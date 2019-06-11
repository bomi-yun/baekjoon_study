#-*- coding: utf-8 -*-

import json
import sys
import math
import Step_Question

class B_Week_5(Step_Question.Step):
    # 완료
    # https://www.acmicpc.net/step/8

    def __init__(self, step):
        self.step = step
        self.initList()

    def initList(self):
        self.step.addList('2438', self.L2438)
        self.step.addList('2292', self.L2292)
        self.step.addList('1193', self.L1193)
        self.step.addList('1011', self.L1011)
        self.step.addList('10250', self.L10250)
        self.step.addList('1927', self.L1927)
        self.step.addList('2775', self.L2775)
        self.step.addList('1475', self.L1475)
        self.step.addList('6064', self.L6064)

    def L2438(self):
        #import sys
        #test
        input = int(sys.stdin.readline().rstrip())
        for i in range(0, input):
            sys.stdout.write('*'*i)

    def L2292(self):
        #import sys
        input = int(sys.stdin.readline().rstrip())
        n = 0
        ret = 1
        
        if input == 1 :  
            n = 1 
        elif input <= 7 :
            n = 2 
        else:
            while ret<input:
                n += 1
                #6*(n-1)+(6*(n-2))
                ret = (6*(n-1))+ret
        print(n)

    def L1193(self):
        #import sys
        input = int(sys.stdin.readline().rstrip())
        ret = 0
        n = 0
        while ret < input:
            n += 1
            ret = ret + n

        s = input - ret

        if n%2 == 1:#홀수
            print(str(abs(s)+1) + "/" + str(n+s))
        else:
            print(str(n+s) + "/" + str(abs(s)+1))

    def L1011(self): #확인필요
        #import sys
        case = int(sys.stdin.readline().rstrip())
        for i in range(0, case):
            ret = 1
            line = sys.stdin.readline().rstrip().split(' ')
            input = int(line[1]) - int(line[0])
            n = 0
            sum = 0
            while True:
                if input < sum+((n+1)*2) : break
                n += 1
                sum += n*2
                print('{0}-{1}<={2}'.format(input, sum, n))
            if input-sum == 0:
                ret = 0
            else :
                ret = input-sum-n
            print(str(n))
            print(str(ret))
            print(str((n*2) + ret))

    def L10250(self):
        #import sys
        case = int(sys.stdin.readline().rstrip())
        for i in range(0, case):
            line = sys.stdin.readline().rstrip().split(' ')
            if int(line[2]) % int(line[0]) == 0:
                print('%d%02d'%(int(line[0]),int(line[2]) / int(line[0])))
            else:
                print('%d%02d' % ((int(line[2]) % int(line[0]), int(line[2]) / int(line[0]) + 1)))

    def L1927(self):
        #import sys
        line = sys.stdin.readline().rstrip().split(' ')
        m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        d = int(line[1])
        for i in range(0, int(line[0])):
            d += m[i]
        print(s[d%7])

    def L2775(self):
        #import sys
        case = int(sys.stdin.readline().rstrip())
        for c in range(0, case):
            row = int(sys.stdin.readline().rstrip()) + 1
            ho = int(sys.stdin.readline().rstrip())
            arr = [[0 for col in range(ho)] for row in range(row)]
            for i in range(0, len(arr)):
                for j in range(0, len(arr[i])):
                    if i == 0:
                        arr[i][j] = j+1
                    elif j == 0 :
                        arr[i][j] = 1
                    else:
                        arr[i][j] = arr[i-1][j] + arr[i][j-1]
            print(arr[row][ho-1])
                    
    def L1475(self):
        #import sys
        #import math
        input = sys.stdin.readline().rstrip()
        l = [0.0]*9
        max = 0
        for i in range(0, len(input)):
            tmp = int(input[i])
            if tmp == 9 or tmp == 6:
                l[6] += 1
            else:
                l[tmp] += 1
                if l[tmp] > max :
                    max = l[tmp]
        l[6] = math.ceil(l[6]/2)
        if l[6] > max : max = l[6]
        sys.stdout.write(str(int(max)))
        
    def L6064(self):
        #import sys
        case = int(sys.stdin.readline().rstrip())
        for c in range(0, case):
            M, N, a, b = map(int, sys.stdin.readline().rstrip().split(' '))
            max = M #최소공배수
            while max % N != 0:
                max += M
            tmp = 0
            ret = -1
            for i in range(0, max/M):
                tmp = M*i+a
                if (tmp - b) % N == 0:
                    ret = tmp
            sys.stdout.write(str(ret))
                
