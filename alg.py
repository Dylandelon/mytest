#!/usr/bin/python3
import logging,sys

# logger = logging.getLogger("log")

# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

def myfn(n):
    if n == 0:
        return 1
    return n * myfn(n-1)

print("lalal=",myfn(10))

def hanoi(n,froma,bufferb,toc):
    if n == 1:
        print("将盘子 %d 从 %s ----->  %s" %(n, froma, toc))
    else:
        hanoi(n - 1,froma,toc,bufferb)
        print("将盘子%d从 %s -----> %s" %(n, froma, toc))
        hanoi(n - 1, bufferb, froma, toc)
        # print("将盘子%d从 %s -----> %s", n, bufferb, toc)
hanoi(4,'a','b','c')




