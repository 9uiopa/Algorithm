T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    x = n-m
    y = m - x
    print(f'#{test_case} {y} {x}')
    
