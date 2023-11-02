for i in range(int(input())):
    n = int(input())
    d = list(map(int,input().split()))
    c = 0
    for j in d:
        if j >=1000:
            c += 1
    print(c)