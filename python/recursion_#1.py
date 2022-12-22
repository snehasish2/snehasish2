def loop(i):
    print(i)
    if i==0:
        return None
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i,"prime")
    else:
        print(i,"composite")        
    loop(i-1)
loop(10)
