temps=[32,30,28,35,31,29,27]
lowest=temps[0]
for t in temps:
    if t<lowest:
        lowest=t
print("Lowest temperature:",lowest)
