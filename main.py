#-*- coding: utf-8 -*-
import Week_2
import Week_4
import Week_5
import Week_6
import scrap_question
import Step_Question

s = scrap_question.Scrap()
s.print_step(8)
step = Step_Question.Step()
b = Week_2.B_Week_2(step)
c = Week_4.B_Week_4(step)
d = Week_5.B_Week_5(step)
f = Week_6.B_Week_6(step)


print(u"* 문제번호 입력 : ")
no = raw_input()
s.print_question(no)
step.excute(no)