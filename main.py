#-*- coding: utf-8 -*-
import Week_2
import scrap_question

s = scrap_question.Scrap()
s.print_step(4)
b = Week_2.B_Week_2()


print(u"* 문제번호 입력 : ")
no = raw_input()
s.print_question(no)
b.excute(no)