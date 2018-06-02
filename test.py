import sys

def eratosthenes(end):
    #에라토스테네스
    list = [True] * (end+1)
    list[0] = False
    if end >= 1 : list[1] = False
    n = 1

    if end > 2 :
        while n < end/2:
            n += 1
            if list[n]: 
                for i in range(n*n, end+1, n):
                    list[i] = False
    return list  

case = int(sys.stdin.readline().rstrip())
arr = [0 for i in range(0, case)]
max = 0

for i in range(0, case):
    arr[i] = int(sys.stdin.readline().rstrip())   
    if max < arr[i] : max = arr[i]
list = eratosthenes(max)

for n in arr:
    tmp = n/2
    while tmp >= 2:  
        if list[tmp] and list[n-tmp] :
            print('{0} {1}'.format(tmp, n-tmp))   
            break
        tmp -= 1    