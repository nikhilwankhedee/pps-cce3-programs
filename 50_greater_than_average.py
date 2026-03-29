nums=[10,20,30,40,50]
avg=sum(nums)/len(nums)
count=0
for n in nums:
    if n>avg:
        count+=1
print("Greater than average:",count)
