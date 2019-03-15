#!/usr/bin/python3

def partition(data,left,right):
    temp = data[left]
    while left < right:
        while left < right and data[right] >= temp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= temp:
            left += 1
        data[right] = data[left]
    data[left] = temp
    return left
# 操作顺序，操作值  指针动态变化
def quickSort(data,left,right):
    if left < right:
        mid = partition(data,left,right)
        quickSort(data,left,mid-1)
        quickSort(data,mid+1,right)
    return data

nums = [5,2,45,6,8,2,1]
print(nums)
print(quickSort(nums,0,len(nums)-1))
print(nums)
