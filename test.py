#-*- coding: utf-8 -*-
list = [False]*10000
i = 1
sum = 0
while sum<10000:
    sum = i
    pow = 10
    tmp = i
    
    while i/pow > 0:
        sum += tmp%pow
        tmp -= tmp%pow
        pow *= 10
    print(str(sum))

    #이미 생성자가 있는 셀프넘버를 만나면 멈춤
    if list[sum] == True:
        for a in range(i, len(list)):
            if list[a] == False:
                i = a
                a = len(list)
    else:
        list[sum] = True
        i = sum

for i in range(i, len(list)):
    if list[i] == False:
        print(str(i))