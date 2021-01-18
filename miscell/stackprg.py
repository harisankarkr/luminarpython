size=int(input("enter the size"))
stk=[]
top=0
n=1
def push(element):
    global top

    if(top>=size):
        print("stack is full")
    else:
        stk.insert(top,element)
        print("element pushed")
        top+=1

def pop():
    global top
    if(top<0):
        print("pop....")
    else:
        print(stk[top],"popped")
        top=top-1
def display():
    print("display...")

while(n!=0):
    option=int(input("enter operation u want to perform 1-push 2-pop 3-display"))
    if(option==1):
        element=input("enter element")
        push(element)
    elif(option==2):
        pop(element)
    elif(option==3):
        display(pop)
    else:
        print("press any key to continue")
        print("or press 0 to exit ......")