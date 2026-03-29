students={"Amit":60,"Rahul":45,"Priya":70,"Riya":30}
count=0
for s in students:
    if students[s]>=50:
        count+=1
print("Students passed:",count)
