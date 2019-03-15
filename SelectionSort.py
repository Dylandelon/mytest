#!/usr/bin/python3
def selectionSort(list):
    n = len(list)
    for i in range(n-1):
        small = i;
        for j in range(i+1,n): # 依次循环遍历，每次只能一个值比一次
            if list[j] < list[small]:
                small = j
        list[i], list[small] = list[small], list[i]
    return list
nums = [5,2,45,6,8,2,1]
print(nums)
print(selectionSort(nums))

