def codediv3(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    total = 0
    s = input()
    list = s.split()
    for j in list:
       
        total += int(j)
    if(total<b):
        return 0
    elif(total>=b):
        if(total//b<c):
            return total//b
        elif(total//b>=c):
            return c
if __name__ == "__main__":
    n = int(input())
    for i in range(0,n):
        a,b,c = input().split()  
        print(codediv3(a,b,c))                    