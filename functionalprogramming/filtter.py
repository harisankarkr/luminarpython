lst=[10,11,12,13,14,15]

even=list(filter(lambda no:no%2==0,lst))
print(even)

employees=["ajay","vijay","anu","tom","joy"]
upp=list(map(lambda name:name.upper(),employees))
print(upp)

nma=list(filter(lambda name:name[0]=='a',employees))
print(nma)
