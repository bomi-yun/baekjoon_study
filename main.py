#-*- coding: utf-8 -*-
import Week_2
import Week_4
import scrap_question
import Step_Question

s = scrap_question.Scrap()
s.print_step(6)
step = Step_Question.Step()
b = Week_2.B_Week_2(step)
c = Week_4.B_Week_4(step)


print(u"* 문제번호 입력 : ")
no = raw_input()
s.print_question(no)
step.excute(no)