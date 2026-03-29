students={"A":65,"B":90,"C":85}
top=""
high=0
for s in students:
    if students[s]>high:
        high=students[s]
        top=s
print("Top:",top)
