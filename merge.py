import sys

case = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for col in range(case)]

first = 0
last = len(arr)-1

mergeSort(arr, first, last)

for i in arr:
    print(str(i))

def mergeSort(self, arr, first, last):
    middle = (first+last)/2
    if first < last :
        self.mergeSort(self.arr, first, middle)
        self.mergeSort(self.arr, middle+1, last)
        self.merge(arr, first, middle, last)

def merge(self, arr, first, middle, last):
    tmp = [0 for i in range(len(arr))]
    i = first #첫번째배열 커서
    j = middle+1 #두번째배열 커서
    cur = first

    while cur <= last:
        if i > middle : #첫 배열이 끝나면
            tmp[cur] = arr[j]
            j += 1
        elif j > last: #두번째 배열이 끝나면
            tmp[cur] = arr[i]
            i += 1
        elif arr[i] > arr[j] :
            tmp[cur] = arr[j]
            j += 1
        elif arr[i] <= arr[j] :
            tmp[cur] = arr[i]
            i += 1
        cur += 1
        
    for i in range(first, last+1):
        self.arr[i] = tmp[i]