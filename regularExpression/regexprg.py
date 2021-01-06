#regular expression
#pattern matching
#package not in bultins.py it is in re

import  re
matcher=re.finditer("ab","abababababaababbababb")
cnt=0
for match in matcher:
    print(match.start())
    cnt+=1
print("total count",cnt)
