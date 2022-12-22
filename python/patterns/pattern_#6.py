def triangle(N):
    s=N-1
    for i in range(1,N+(N-1),2):
        print(" "*s,"i"*i," "*s)
        s=s-1
k=int(input("enter ur pyramid height in units"))
triangle(k)



    