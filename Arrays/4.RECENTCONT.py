for _ in range(int(input())):
    n = int(input())
    l = list(input().split())
    c1 = 0 
    c2 = 0
    for i in l:
        if i == 'START38':
            c1 += 1 
        else:
            c2 += 1 
    print(c1,c2)