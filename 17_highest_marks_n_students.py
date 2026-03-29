n=int(input("Enter students:"))
marks=[]
for i in range(n):
    marks.append(int(input("Enter marks:")))
highest=marks[0]
for m in marks:
    if m>highest:
        highest=m
print("Highest:",highest)
