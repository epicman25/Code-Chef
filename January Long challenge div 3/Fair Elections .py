
for i in range(int(input())):
    a,b = map(int,input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    count = 0
    x=True
    if(sum(l1)>sum(l2)):
        print(0)
    else:
        while(sum(l1)<=sum(l2)):
            l1.sort()
            l2.sort(reverse=True)
            if(l1[0]<l2[0]):
                temp = l1[0]
                l1[0] = l2[0]
                l2[0] = temp   
                count+=1
            else:
                x=False
                print(-1)
                break
        if(x==True):
            print(count)         
    