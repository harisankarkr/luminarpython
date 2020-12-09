lst=[1,2,3,4]
num=int(input("enter your number :"))
sum=0
for i in lst:
    for j in lst:
        if (i==j):
            continue
        elif(i+j==a):
            print(i,j)
            break
