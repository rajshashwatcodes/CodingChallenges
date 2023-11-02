for i in range(int(input())):
    n,m = list(map(int,input().split()))
    print(n-m if n-m > 0 else 0)