class employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name

f=open("employee","r")
lst=[]
for lines in f:
    id, name, exp, salary, desig=lines.rstrip("\n").split(",")

    ob=employee(id,name,exp,salary,desig)
    lst.append(ob)

for emp in lst:
    print(emp)

upp=list(map(lambda emp:emp.name.upper(),lst))
print(upp)

devp=list(filter(lambda emp:emp.desig=='developer',lst))
for emp in devp:
    print(emp)

sal=list(filter(lambda emp:int(emp.salary)>23000,lst))
for emp in sal:
    print(emp)