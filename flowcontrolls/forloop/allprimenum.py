lowlimit=int(input("enter the lower limit :"))
uplimit=int(input("enter the upper limit :"))
for num in range(lowlimit,uplimit+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
            else:
                print(num)