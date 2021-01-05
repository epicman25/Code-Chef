l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'o','p']
for _ in range(int(input())):
    len = int(input())
    str = input()
    for i in range(0,len,4):
        print(l[int((str[i:i+4]),2)],end="")
    print("\n")    
