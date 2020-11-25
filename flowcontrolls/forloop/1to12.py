#for i in range(1,13):
 #   print(i,end="\t")
  #  if i%4==0:
   #     print("\n")

cnt=0
for i in range(1,13):
    print(i,end="\t")
    cnt += 1
    if cnt==4:
        print()
        cnt=0
