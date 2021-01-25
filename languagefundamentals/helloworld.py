# print("program for swapping")
#
# val1 = input("enter value of 1 :")
# val2 = input("enter value of 2 :")
#
# print("before swapping")
# print(val1)
# print(val2)
#
# temp=val1
# val1=val2
# val2=temp
#
# print("after swapping")
# print(val1)
# print(val2)
#
# val3=input("press enter key to exit")

num=int(input("enter a number:"))
fact=1
for i in range (1,num+1):
	fact = fact*i
	num=num-1
print(fact)