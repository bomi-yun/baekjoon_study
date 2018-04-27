#-*- coding: utf-8 -*-
import Level_2
import requests

#b = Level_2.B_Level_2()

r = requests.get("https://www.acmicpc.net/problem/2742")
print(r.text)
