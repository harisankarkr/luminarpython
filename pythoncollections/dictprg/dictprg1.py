
employee={"eid":1000,"desig":"developer","exp":1,"company":"luminar"}

print(employee["company"])

print("salary" in employee)

employee["salary"]=30000
print(employee)

employee["salary"]+=5000
print(employee["salary"])

for k,v in employee.items():
    print(k,v)