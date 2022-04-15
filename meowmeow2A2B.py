import builtins
import random
import math
from sre_constants import JUMP
from tkinter import N
x = random.randint(0,9)

nums = [0,1,2,3,4,5,6,7,8,9]
bnum = [0,0,0,0]
play = True
random.shuffle(nums)
while play:
    print (nums)
    a = 0
    b = 0
    l = 0
    p = 0
    op = input("enter four numbers:")
        
    y = [int(k) for k in str(op)]
    for i in range(0,4):
        bnum[i]=nums[i]
        if (nums[i] == y[i]):
            a += 1
    bnum.sort()
    y.sort()
    n = 0
    m = 0

    for i in range(0,4):
        if (i+n>44):
            break
        if (i+m>4):
            break
        if (bnum[i+n] < y[i+m]):
            n += 1
            i -= 1
            continue
        if (bnum[i+n] > y[i+m]):
            m += 1
            i -= 1
            continue
        if (bnum[i+n] == y[i+m]):
            b += 1
    print (a," ",b)
    b=b-a
    print ("A",a,"B",b)
    if (a==4):
        play = False
print ("yee")
