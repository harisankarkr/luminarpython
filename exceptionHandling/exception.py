no1=int(input("enter number one:"))
no2=int(input("enter number two:"))

try:
    res=no1/no2
    print(res)
except:
    print("division is not possible for this number")

try:
    res=no1+no2
    print(res)
except:
    print("addition is not possible")

finally:
    print("thank you")
    print("visit again")