#!/usr/bin/python3

def insertionSort(list):
    for i in range(1,len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = temp
    return list

nums = [5,2,45,6,8,2,1]
print(nums)
print(insertionSort(nums))
