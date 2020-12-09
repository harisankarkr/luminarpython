lst=[21,28,18,22,7,2,25]
lst.sort()
low=0
upp=len(lst)-1
flag=0
element=int(input("enter element you want to search :"))
while(low<=upp):
    mid=(low+upp//2)
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if flag==0:
    print("no element")
else:
    print("element found")