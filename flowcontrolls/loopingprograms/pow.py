num=int(input("enter a number :"))
sum=0
while(num!=0):
    mod=num%10
    num= num//10
    mod1=mod**3
    sum=sum+mod1
print(sum)
