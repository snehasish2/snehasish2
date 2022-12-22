ar=[22,100,3,200,1,34,2,99,0,34]
l=len(ar)
for k in range (0,len(ar)):
    for i in range (0,l-1):
            if ar[i+1]<ar[i]:
                j=ar[i+1]
                ar[i+1]=ar[i]
                ar[i]=j
            print(ar) 
    l-=1
    


