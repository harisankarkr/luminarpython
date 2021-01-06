from re import *

#predefined charatcer set
#pattern='[a-z]'
#pattern='[0-9]'
#pattern='[^0-9]'
#pattern='[a-zA-Z]'
#pattern='[a-zA-z0-9]'
#pattern='[^a-zA-Z0-9 ]'


#pre defined character
#pattern="\s" #chk for space
#pattern="\S" #chk for ^space
#pattern="\d" #digits
#pattern="\D" #^digits
#pattern="\w" #[a-zA-z0-9]
#pattern="\W" #[^a-zA-z0-9]


mather=finditer(pattern,"abc Z@7k")
for match in mather:
    print(match.start())
    print(match.group())