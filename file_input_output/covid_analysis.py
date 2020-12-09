f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[3].rstrip("***")
    cofirned_cases=int(words[8])
    if(state not in dict):
        dict[state]=cofirned_cases
    else:
        dict[state]=cofirned_cases
for k,v in dict.items():
    print(k,"--->",v)

high=max(dict,key=dict.get)
print(high)