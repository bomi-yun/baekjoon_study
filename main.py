#-*- coding: utf-8 -*-
import Level_2
import scrap_question

s = scrap_question.Scrap()
s.print_step(3)
b = Level_2.B_Level_2()


print(u"* 문제번호 입력 : ")
no = raw_input()
s.print_question(no)
b.excute(no)