import random

nums = [0,1,2,3,4,5,6,7,8,9]
play = True
random.shuffle(nums)
print ("answer: ",nums)
while play:
    a = 0
    b = 0
    p = [0,0,0,0,0,0,0,0,0,0]
    op = input("enter four numbers:")
    y = [int(k) for k in op]
    for i in range(0,4):
        p[nums[i]] += 1
        if (nums[i] == y[i]):
            a += 1
    print (p) 
    for i in range(0,4):
        if (p[y[i]]>0):
            p[y[i]] += 1
    print (p) 
    for i in range(0,10):
        if (p[i]>1):
            b += 1
    b=b-a
    print ("A",a,"B",b)
    if (a==4):
        play = False
print ("yee")
