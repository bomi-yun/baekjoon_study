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
        self.step.addList('2751', self.L2751)
        self.step.addList('10987', self.L10987)
        self.step.addList('2108', self.L2108)
        self.step.addList('1427', self.L1427)
        self.step.addList('1181', self.L1181)

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

    def L2751(self): #합병정렬, 런타임에러 
        # self.arr = [120, 500, 5, 3, 7, 8, 0, 1, 2, 10, 4, 55]
        
        case = int(sys.stdin.readline().rstrip())
        self.arr = [int(sys.stdin.readline().rstrip()) for col in range(case)]

        first = 0
        last = len(self.arr)-1
        
        self.mergeSort(self.arr, first, last)
        
        for i in self.arr:
            print(str(i))

    def mergeSort(self, arr, first, last):
        middle = (first+last)/2
        if first < last :
            self.mergeSort(self.arr, first, middle)
            self.mergeSort(self.arr, middle+1, last)
            self.merge(arr, first, middle, last)

    def merge(self, arr, first, middle, last):
        tmp = [0 for i in range(len(arr))]
        i = first #첫번째배열 커서
        j = middle+1 #두번째배열 커서
        cur = first
        
        while cur <= last:
            if i > middle : #첫 배열이 끝나면
                tmp[cur] = arr[j]
                j += 1
            elif j > last: #두번째 배열이 끝나면
                tmp[cur] = arr[i]
                i += 1
            elif arr[i] > arr[j] :
                tmp[cur] = arr[j]
                j += 1
            elif arr[i] <= arr[j] :
                tmp[cur] = arr[i]
                i += 1
            cur += 1
            
        for i in range(first, last+1):
            self.arr[i] = tmp[i]

    def L10987(self): #메모리초과
        case = int(sys.stdin.readline().rstrip())
        arr = [int(sys.stdin.readline().rstrip()) for col in range(case)]
        # bucket = [[[] for i in range(0, 9)]]
        bucket = []
        count = case
        pow = 1
        c=0
        flag = True
        while flag:
            for i in range(0, len(arr)):
                if pow == 1 : c = arr[i]%10
                else : c = arr[i] / pow % pow
                bucket[c].append(arr[i])
            pow *= 10
            
            arr = []
            for i in range(0, len(bucket)):
                if len(bucket[i]) > 0 : 
                    arr += bucket[i]
                if i == 0 and len(bucket[i]) == count:
                    flag = False
                bucket[i] = []
        
        for i in arr:print(str(i))

    def L2108(self):
        case = int(sys.stdin.readline().rstrip())
        arr = [0]*case
        sum = 0
        for col in range(case):
            arr[col] = int(sys.stdin.readline().rstrip())
            sum += arr[col]
        avg = sum / case #평균
        #정렬
        for i in range(0, len(arr)):
            min = 100000
            cur = 0
            for j in range(i+1, len(arr)):
                if arr[j] < min :
                    min = arr[j]
                    cur = j
            if min < arr[i]:
                tmp = arr[cur]
                arr[cur] = arr[i]
                arr[i] = tmp

        print(avg)
        #중앙
        print(arr[len(arr)/2])
        #최빈
        c = 0
        max = 0
        if len(arr) > 1: ret = arr[1]
        else : ret = arr[0]
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i] : 
                c += 1
                if max == c : ret = arr[1]
                elif max < c : 
                    max = c
                    ret = arr[i]
            else : 
                c = 0
        print(ret)
        #범위
        print(arr[len(arr)-1] - arr[0])


    def L1427(self):
        input = sys.stdin.readline().rstrip()
        arr = [int(input[i]) for i in range(0, len(input))]

        for i in range(0, len(arr)):
            max = 0
            cur = 0
            for j in range(i+1, len(arr)):
                if arr[j] > max :
                    max = arr[j]
                    cur = j
            if max > arr[i]:
                tmp = arr[cur]
                arr[cur] = arr[i]
                arr[i] = tmp
        
        for i in range(0, len(arr)):
            sys.stdout.write(str(arr[i]))


    def L1181(self):
        case = int(sys.stdin.readline().rstrip())
        arr = [sys.stdin.readline().rstrip() for col in range(case)]

        bucket = {}
        for i in range(0, len(arr)):
            if bucket.get(len(arr[i])) == None:
                bucket[len(arr[i])] = []
            bucket[len(arr[i])].append(arr[i])
            
        for b in sorted(bucket.keys()):
            bucket[b].sort()
            for j in range(0, len(bucket[b])):
                if j == 0 or (j > 0 and bucket[b][j-1] != bucket[b][j]) :
                    print(bucket[b][j])
        

