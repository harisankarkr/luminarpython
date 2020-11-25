num=int(input("enter a number :"))
nmin=int(input("enter a min number :"))
nmax=int(input("enter a max number :"))
for i in range(1,nmax+1):
    if i**num in range(nmin,nmax+1):
        print(i,"^",num,"=",i**num)
