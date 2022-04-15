import random

nums = [0,1,2,3,4,5,6,7,8,9]
play = True
random.shuffle(nums)
while play:
    print (nums)
    a = 0
    b = 0
    e = 0
    g = 0
    op = input("enter four numbers:")
    l = len (op)
    if (l != 4):
        print ("invalid value")
        continue
    y = [int(k) for k in op]
    for i in range (0,3):
        e += 1
        for j in range (e,4):
            if (y[i]==y[e]):
                print ("invalid value")
                g += 1
                if (g>0):       
                    break
        if (g>0):
            break        
    if (g>0):
        continue
    for i in range(0,4):
        if (nums[i] == y[i]):
            a += 1
    for j in range(0,4):
        for o in range(0,4):
            if (nums[j]==y[o]):
                b += 1
    b=b-a
    print ("A",a,"B",b)
    if (a==4):
        play = False
print ("yee")
