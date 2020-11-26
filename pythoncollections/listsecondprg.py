limit=int(input("enter limit "))
even=[]
odd=[]
for i in range(1,limit+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)