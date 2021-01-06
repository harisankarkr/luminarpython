# age=int(input("enter your age:"))
#
# if age<18:
#     raise Exception("sorry invalid age")

num=input("enter a number:")
if type(num)==int:
    print("ok")
else:
    raise Exception("only inegers allowed")