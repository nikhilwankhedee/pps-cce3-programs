nums=[10,-5,20,-3,15]
pos=0
neg=0
for n in nums:
    if n>=0:
        pos+=1
    else:
        neg+=1
print("Positive:",pos)
print("Negative:",neg)
