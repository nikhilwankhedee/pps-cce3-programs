students={"Amit":80,"Rahul":92,"Priya":88}
top=""
high=0
for s in students:
    if students[s]>high:
        high=students[s]
        top=s
print("Topper:",top)
