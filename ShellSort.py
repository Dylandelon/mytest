#!/usr/bin/python3
def shell_sort(li):
    gap = int(len(li)//2)   # 初始把列表分成 gap个组，但是每组最多就两个元素，第一组可能有三个元素
    while gap >0:
        for i in range(gap,len(li)):
            print("gap:", gap)
            print("i:",i)
            tmp = li[i]
            j = i - gap
            print("j:",j)

    return li
nums = [5,2,45,6,8,2,1]
shell_sort(nums)
