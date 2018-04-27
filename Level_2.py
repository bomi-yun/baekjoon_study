#-*- coding: utf-8 -*-

import json
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

    