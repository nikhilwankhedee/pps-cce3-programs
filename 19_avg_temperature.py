temps=[]
for i in range(7):
    temps.append(int(input("Temp:")))
total=0
for t in temps:
    total+=t
print("Average:",total/7)
