stack=[]
def add(i):
    stack.append(i)
def remove():
    if len(stack)!=0:
        stack.pop()
    else:
        print("under flow")        

add(1)
print(stack)
add(2)
print(stack)
remove()
print(stack)
remove()
print(stack)

remove()
print(stack)
