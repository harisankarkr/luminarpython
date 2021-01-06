#quantifiers

from re import *
#pattern="a+"
#pattern="a*"
#pattern="a?"
#pattern=^a"
#pattern="a$"
#pattern='a{2,3}'

matcher=finditer(pattern,"aaaabaabaaaaa")
for match in matcher:
    print(match.start())
    print(match.group())