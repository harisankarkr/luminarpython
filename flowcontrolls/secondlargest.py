
num1=int(input("enter the value of num1 :"))
num2=int(input("enter the value of num2 :"))
num3=int(input("enter the value of num3 :"))

oder1=0
oder2=0
oder3=0

if(num1>num2)and(num1<num3)or(num1<num2)and(num1>num3):
    print("num1 - ",num1," is the second largest number")
elif(num2>num1)and(num2<num3)or(num2<num1)and(num2>num3):
    print("num2 - ",num2," is the second largest number")
else:
    print("mum3 - ",num3," is the second largest number")

if(num1<num2)and(num1<num3):
    ordr1=num1
if(num2<num1)and(num2<num3):
    ordr1=num2
if(num3<num1)and(num3<num2):
    ordr1=num3

if(num1>num2)and(num1<num3)or(num1<num2)and(num1>num3):
    ordr2=num1
if(num2>num1)and(num2<num3)or(num2<num1)and(num2>num3):
    ordr2=num2
if(num3>num1)and(num3<num2)or(num3<num1)and(num3>num2):
    ordr2=num3

if(num1>num2)and(num1>num3):
    ordr3=num1
if(num2>num1)and(num2>num3):
    ordr3=num2
if(num3>num1)and(num3>num2):
    ordr3=num3

print("given numbers in ascending order :",ordr1,ordr2,ordr3)
print("given numbers in descending order :",ordr3,ordr2,ordr1)

