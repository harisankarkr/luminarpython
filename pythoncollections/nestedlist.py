student=[
    [100,"arun","bca",145],
    [101,"arjun","bca",125],
    [102,"varun","mca",155],
    [103,"annu","mca",165],
    [104,"kiran","bca",145]
]

for student in student:
    print(student[1])
total=0
for student in student:
    total=total+student[3]
    print(total)
for student in student:
    if student[2]=="mca":
        print(student)
