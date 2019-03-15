#!/usr/bin/python3

def merge(list,left,mid,right):
    i = left
    j = mid + 1
    ltmp = []
    while i <= mid and j <= right:
        if list[i] < list[j]:
            ltmp.append(list[i])
            i += 1
        else:
            ltmp.append(list[j])
            j += 1
    while i <= mid:
        ltmp.append(list[i])
        i += 1
    while j <= right:
        ltmp.append(list[j])
        j += 1
    list[left:right+1] = ltmp
    return  list
def _mergeSort(list,left,right):
    if left < right:
        mid = (left + right) // 2
        _mergeSort(list, left, mid)
        _mergeSort(list, mid + 1, right)
        merge(list, left, mid, right)
    return list
def mergeSort(list):
    return _mergeSort(list,0,len(list)-1)
nums = [5,2,45,6,8,2,1]
print(nums)
print(mergeSort(nums))
print(nums)
