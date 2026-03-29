t=(5,10,15,20,25)
key=int(input("Enter number: "))
found=False
for i in t:
    if i==key:
        found=True
print("Found" if found else "Not found")
