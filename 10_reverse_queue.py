queue=[1,2,3,4,5]
rev=[]
for i in range(len(queue)-1,-1,-1):
    rev.append(queue[i])
print(rev)
