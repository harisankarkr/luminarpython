from re import *

f=open("registrationnumbers","r")
fout=open("validreg","w")

regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip("\n"))

rule="KL\d{2}[A-Z]{2,2}\d{1,4}"

for vechilenum in regnum:

    matcher=fullmatch(rule,vechilenum)
    if matcher !=None:
        fout.write(vechilenum+"\n")
    else:
        pass