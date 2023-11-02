for i in range(int(input())):
    n = int(input())
    doll = {}
    for i in range(n):
        d = input().strip()
        if d in doll:
            doll[d] += 1 
        else:
            doll[d] =  1
    for dl,v in doll.items():
        if v%2 != 0:
            print(dl)