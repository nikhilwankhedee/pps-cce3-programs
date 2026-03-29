text=input("Enter string:")
count=0
for c in text:
    if c in "aeiouAEIOU":
        count+=1
print("Vowels:",count)
