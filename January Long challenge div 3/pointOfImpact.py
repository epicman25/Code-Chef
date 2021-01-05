for i in range(int(input())):
    n,m,x,y = map(int,input().split())
    if(x==y):
        print(n,n)
    elif(x>y):
        l1= [x+(n-x),y+((n-x)),y+(n-x),x+(n-x),0,n-(y+(n-x)),n-(y+(n-x)),0] 
        a = ((m-1)%4)*2
        b = a+2
        for i in l1[a:b]:
            print(i,end = ' ')                        
    elif(y>x):
        l2 = [x+(n-y),n,n,x+(n-y),n-(x+(n-y)),0,0,n-(x+(n-y))] 
        a = ((m-1)%4)*2
        b = a+2
        for i in l2[a:b]:
            print(i,end = ' ')
    
       
    
