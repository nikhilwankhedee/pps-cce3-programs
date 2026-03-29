orders=[101,102,103,102,104,101]
dup=[]
for o in orders:
    if orders.count(o)>1 and o not in dup:
        dup.append(o)
print("Duplicates:",dup)
