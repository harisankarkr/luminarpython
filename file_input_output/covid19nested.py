f=open("covid_19_india.csv","r")
covid={}
for lines in f:
    slno,date,time,place,a,b,c,d,total_case=lines.rstrip("\n").split(",")
    if slno not in covid:
        covid[slno]={"slno":slno,"place":place,"total_case":total_case}
    else:
        pass
print(covid)


def print_covid(**kwargs):

    id=kwargs["slno"]
    if(slno in covid):
        print(covid[slno]['total_case'])
        if "property" in kwargs:
            prop=kwargs["property"]
            if(prop in covid[slno]):
                print(covid[slno][prop])
            else:
                print("invalid property")
    else:
        print('slno doesnot exist')

print_covid(slno=4532)
