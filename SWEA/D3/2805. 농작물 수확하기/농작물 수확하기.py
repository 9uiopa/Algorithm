T = int(input())
for t in range(1, T + 1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    mid = int((n-1)/2)
    a = 0
    result = 0
    for r in range(n):
        if 0<r<= mid  : a+=1
        elif r>mid : a-=1
        for c in range(mid-a, mid+1+a):
            result+= farm[r][c]
    print(f'#{t} {result}')