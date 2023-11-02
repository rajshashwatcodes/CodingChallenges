for _ in range(int(input())):
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    c = 0
    for i in h:
        if i > k:
            c += 1
    print(c)