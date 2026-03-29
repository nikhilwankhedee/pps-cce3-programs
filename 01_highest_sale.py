sales=[1200,1500,900,2000,1750]
highest=sales[0]
for s in sales:
    if s>highest:
        highest=s
print("Highest sale:",highest)
