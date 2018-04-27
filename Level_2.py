#-*- coding: utf-8 -*-

import json
class B_Level_2:
    list = []
    def __init__(self):
        self.initList()
        #for o in self.list:
        #    print(o["no"] +" : "+ o["title"])
    
    def excute(self, no):
        for o in self.list:
            if no == o["no"]:
                o["method"]()

    def initList(self):
        self.addList('2741', self.L2741)
        
    def addList(self, obj, method):
        self.list.append({
            "no" : obj,
            "method" : method
        })

    def L2741(self):
        input = int(raw_input())
        for i in range(0, input):
            print(i+1)