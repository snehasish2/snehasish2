for i in range(1,101):
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count+=1
        j+=1        
    if count==2:
        print(i)        
    
