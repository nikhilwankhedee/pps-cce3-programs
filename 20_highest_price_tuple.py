prices=(120,340,250,500)
high=prices[0]
for p in prices:
    if p>high:
        high=p
print("Highest:",high)
