#!/usr/bin/python3

def sift(list,left,right):
    i = left
    j = 2*i + 1
    temp = list[left]
    while j <= right:
        if j+1 <= right and list[j] < list[j+1]:
          j = j+1
        if temp < list[j]:
            list[i] = list[j]
        else:
            break
        i = j
        j = 2*i + 1
        list[i] = temp

def heapSort(list):
    n = len(list)
    for i in range(n//2-1, -1, -1):
        sift(list, i, n-1)
    for i in range(n-1,-1,-1):
        list[i], list[0] = list[0], list[i]
        sift(list, 0, i-1)
    return list


nums = [5,2,45,6,8,2,1]
print(heapSort(nums))