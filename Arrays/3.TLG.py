p1 = 0
p2 = 0
max1 = 0
max2 = 0
for _ in range(int(input())):
    a,b = map(int,input().split())
    max1 += a
    max2 += b
    if max1>max2:
        p1 = max(p1,max1-max2)
    else:
        p2 = max(p2, max2-max1)
if p1 > p2:
    print(1, p1)
else:
    print(2, p2)