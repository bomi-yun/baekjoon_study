#-*- coding: utf-8 -*-

import json
import sys

class B_Level_2:
    list = []
    def __init__(self):
        self.initList()
        #for o in self.list:
        #    print(o["no"] +" : "+ o["title"])
    
    def excute(self, no):
        print(str(no) + u"실행")
        for o in self.list:
            if no == o["no"]:
                o["method"]()

    def initList(self):
        self.addList('2741', self.L2741)
        self.addList('2742', self.L2742)
        self.addList('2739', self.L2739)
        self.addList('2438', self.L2438)
        self.addList('2439', self.L2439)
        self.addList('2440', self.L2440)
        self.addList('2441', self.L2441)
        self.addList('1924', self.L1924)
        self.addList('8393', self.L8393)
        self.addList('11720', self.L11720)
        self.addList('11721', self.L11721)
        self.addList('15552', self.L15552)
        self.addList('9498', self.L9498)
        self.addList('10817', self.L10817)
        self.addList('10871', self.L10871)
        self.addList('1546', self.L1546)
        self.addList('4344', self.L4344)
        self.addList('1110', self.L1110)
        
    def addList(self, obj, method):
        self.list.append({
            "no" : obj,
            "method" : method
        })

    def L2741(self):
        input = int(raw_input())
        for i in range(0, input):
            print(i+1)

    
    def L2742(self):
        input = int(raw_input())
        for i in reversed(range(0, input)):
            print(i+1)

    def L2739(self):
        input = int(raw_input())
        for i in range(1, 10):
            print '{0} * {1} = {2}'.format(str(input), str(i), str(input * i))

    def L2438(self):
        input = int(raw_input())
        for i in range(1, input+1):
            print '*'*i
            
    def L2439(self):
        input = int(raw_input())
        for i in range(1, input+1):
            print '{0}{1}'.format(' '*(input-i), '*'*i)
            
    def L2440(self):
        input = int(raw_input())
        for i in reversed(range(1, input+1)):
            print '*'*i

    def L2441(self):
        input = int(raw_input())
        for i in reversed(range(1, input+1)):
            print '{0}{1}'.format(' '*(input-i), '*'*i)

    def L1924(self):
        input = raw_input()
        month = int(input.split(' ')[0])
        day = int(input.split(' ')[1])
        tmp = 0

        months = [0 ,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(0, month):
            tmp += months[i]

        days = (tmp + day) % 7
        if days == 0 : print("SUN")
        elif  days == 1 : print("MON")
        elif days == 2 : print("TUE")
        elif days == 3 : print("WED")
        elif days == 4 : print("THU")
        elif days == 5 : print("FRI")
        elif days == 6 : print("SAT")

    def L8393(self):
        input = int(raw_input())
        sum = 0
        for i in range(1, input+1):
            sum += i
        print(str(sum))

    def L11720(self):
        count = int(raw_input())
        input = raw_input()
        sum = 0

        for i in range(0, count):
            sum += int(input[i:i+1])
        print(sum)
    
    def L11721(self):
        input = raw_input()
        for i in range(0, len(input), 10):
            print(input[i:i+10])

    def L15552(self): #메모리초과
        l = ""
        for i in range(0, int(sys.stdin.readline().rstrip())):
            l += str(sum(map(int, sys.stdin.readline().rstrip().split(' ')))) + '\n'
        print(l[0:-1])
    
    def L9498(self):
        input = int(sys.stdin.readline().rstrip())
        if input >= 90 :
            print("A")
        elif input >= 80:
            print("B")
        elif input >= 70:
            print("C")
        elif input >= 60:
            print("D")
        else:
            print("F")

    def L10817(self):
        input = sys.stdin.readline().rstrip()
        a = int(input.split(' ')[0])
        b = int(input.split(' ')[1])
        c = int(input.split(' ')[2])
        if (a>=b and a<=c) or (a>=c and a<=b):
            print(str(a))
        elif (b>=a and b<=c) or (b>=c and b<=a):
            print(str(b))
        elif (c>=a and c<=b) or (c>=b and c<=a):
            print(str(c))
    
    def L10871(self): #ㅅㅣ간초과
        input = sys.stdin.readline().rstrip()
        count = int(input.split(' ')[0])
        chk = int(input.split(' ')[1])
        input = sys.stdin.readline().rstrip()

        for i in range(0, count): 
            if int(input.split(' ')[i]) < chk:
                print(input.split(' ')[i]),

    def L1546(self): #틀렸


    def L4344(self):
        count = int(sys.stdin.readline().rstrip())
        input = ""
        l = []
        n = 0
        for i in range(0, count):
            sum = 0
            avg = 0
            l = sys.stdin.readline().rstrip().split(' ')
            n = int(l[0])
            l = l[1:len(l)]
            for j in range(0, len(l)): sum += int(l[j])
            avg = sum/n
            sum = 0
            for j in l: 
                if int(j) > avg : sum += 1
            print("{0}%".format("%0.3f" %(float(sum)/float(n)*100)))

    def L1110(self):
        input = int(sys.stdin.readline())
        tmp = input
        ret = 0
        while True:
            tmp = (tmp%10*10) + ((tmp/10 + tmp%10) % 10)
            ret += 1
            if input == tmp : break
        print(ret)




