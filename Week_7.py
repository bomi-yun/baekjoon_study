#-*- coding: utf-8 -*-

import json
import sys
import Step_Question

class B_Week_7(Step_Question.Step):
    # 완료
    # https://www.acmicpc.net/step/10

    def __init__(self, step):
        self.step = step
        self.initList()

    def initList(self):
        self.step.addList('1978', self.L1978)
        self.step.addList('2581', self.L2581)
        self.step.addList('1929', self.L1929)
        self.step.addList('4948', self.L4948)
        self.step.addList('9020', self.L9020)

    def L1978(self):
        #import sys
        case = int(sys.stdin.readline().rstrip())
        line = sys.stdin.readline().rstrip()
        list = [int(line.split(' ')[i]) for i in range(0, case)]
        count = 0
        for n in list :
            check = False
            if n <= 2 :
                if n == 2 :
                    count += 1
            else : 
                i = 2
                while i <= n/2:
                    if n % i == 0 : 
                        check = True
                        break
                    i+=1
                if check == False :
                    count += 1 
        print(count)

    #2, 3을 거치는 동안 2*5, 3*5가 계산되었다(4는 소수 아님)
    #-> 5의 배수를 계산할때는 5*2, 5*3계산하지 않는다
    #-> 5*5부터 시작
    def eratosthenes(self, end):
        #에라토스테네스
        list = [True] * (end+1)
        list[0] = False
        if end >= 1 : list[1] = False
        n = 1

        if end > 2 :
            while n < end/2:
                n += 1
                if list[n]: 
                    for i in range(n*n, end+1, n):
                        list[i] = False
        return list  

    def L2581(self):
        start = int(sys.stdin.readline().rstrip())
        end = int(sys.stdin.readline().rstrip())
        
        list = self.eratosthenes(end)
        min = 0
        sum = 0
        for i in range(start, end+1):
            if list[i] == True:
                sum += i
                if min == 0 : min = i
        if min == 0 :
            sys.stdout.write("-1")
        else:
            sys.stdout.write(str(sum) + "\n")
            sys.stdout.write(str(min))

    def L1929(self):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        list = self.eratosthenes(end)
        for i in range(start, end+1):
            if(list[i] == True):
                sys.stdout.write(str(i) + "\n")

    def L4948(self):
        arr = []
        max = 0
        while True:
            input = int(sys.stdin.readline().rstrip())
            if input == 0 : break
            if input > max : max = input
            arr.append(input)
            
        list = self.eratosthenes(max*2)
        
        for i in arr:
            count = 0
            for j in range(i+1, i*2+1):
                if list[j] : count += 1
            sys.stdout.write(str(count) + "\n")    

    def L9020(self):
        case = int(sys.stdin.readline().rstrip())
        arr = [0 for i in range(0, case)]
        max = 0

        for i in range(0, case):
            arr[i] = int(sys.stdin.readline().rstrip())   
            if max < arr[i] : max = arr[i]
        list = eratosthenes(max)

        # 3 = 1+2 = 2+1 -> n/2만 계산해도 된다
        # 두 수의 차이가 제일 적은 값을 리턴하기 때문에 n/2부터 값을 찾는다
        for n in arr:
            tmp = n/2
            while tmp >= 2:  
                if list[tmp] and list[n-tmp] :
                    print('{0} {1}'.format(tmp, n-tmp))   
                    break
                tmp -= 1    