#for row in range(1,4):
 #   for col in range(1,4):
  #      print(col,end="\t")
   # print()

#for row in range(0,5):
 #   for col in range(0,row):
  #      print("*",end="\t")
   # print()


#for row in range(1,5):
 #   for col in range(1,row+1):
  #      print(row,end="\t")
   # print()

#for row in range(1,5):
 #   for col in range(1,row+1):
  #      print(col,end="\t")
   # print()

for row in range(1,5):
    for col in range(1,8):
        if row==4 or row+col==5 or col-row==3:
            print("*",end="")
        else:
            print(end=" ")
    print()
