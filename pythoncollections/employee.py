employees=[[1001,"ajay","qa",1981,2003],
[1002,"vijay","developer",1992,2008],
[1003,"arun","ba",1989,2010],
[1004,"amal","developer",2009,2014],
[1004,"vimal","developer",1987,1989],
]

for employee in employees:
    print(employee[2])

for employee in employees:
    if employee[2]=="developer":
        print(employee)
