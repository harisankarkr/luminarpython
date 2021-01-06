from functools import *
isl=[
    {"team":"mumbaicity","mp":7,"win":5,"drawn":1,"loss":1,"gf":11,"ga":3,"pts":16},
    {"team":"atkmohanbagan","mp":7,"win":5,"drawn":1,"loss":1,"gf":8,"ga":3,"pts":16},
    {"team":"benguluru","mp":7,"win":3,"drawn":3,"loss":1,"gf":11,"ga":8,"pts":12},
    {"team":"northeast","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":6,"pts":10},
    {"team":"jemshedhpur","mp":7,"win":2,"drawn":4,"loss":1,"gf":8,"ga":7,"pts":10}
]

teams=list(map(lambda team:team["team"].upper(),isl))
print(teams)

points=reduce(lambda p1,p2:p1 if p1>p2 else p2,
              list(map(lambda team:team["pts"],isl)))
print(points)

#min
#high win
