employee={}
f=open("employee","r")
def emp(*eid):
    for lines in f:
        employee=lines.rstrip("\n").split(",")
        id=employee[0]
        if id in employee:
            print(employee[1])

emp()