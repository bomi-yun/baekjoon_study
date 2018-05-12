#-*- coding: utf-8 -*-

import json
import sys

class Step: #백준 단계별 풀어보기 부모클래스
    list = []
    def __init__(self):
        pass

    def addList(self, obj, method):
        self.list.append({
            "no" : obj,
            "method" : method
        })
    
    def getList(self):
        return self.list

    def excute(self, no):
        print(str(no) + u"실행")
        for o in self.list:
            if no == o["no"]:
                o["method"]()

    def printNo(self):
        for o in self.getList():
            print("{0}".format(o.no))