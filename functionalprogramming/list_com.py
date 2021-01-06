#lst=[1,2,3,4,5,6,7,8]
#data=[i+1 if i>5 else i-1 for i in lst]
#print("output",data)

#flatten operation
matrix=[[1,2,3],[4,5,6],[7,8,9]]
data1=[j for i in matrix for j in i ]
print("output",data1)