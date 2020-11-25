lowlimit=int(input("enter the  low limit :"))
uplimit=int(input("enter the  low limit :"))
sum=0
sum1=0
while(lowlimit<=uplimit):
    if(lowlimit%2==0):
        sum=sum+lowlimit
    lowlimit+=1
print("sum of even numbers", sum)

while(lowlimit<=uplimit):
    if(lowlimit%2!=0):
        sum1=sum1+lowlimit
    lowlimit+=1
print("sum of odd numbers", sum1)