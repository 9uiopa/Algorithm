T = int(input())
for test_case in range(1, T + 1):
    n,k = map(int, input().split())
    scores = list(map(int,input().split()))
    sum = 0
    scores.sort(reverse = True)
    for i in range(k):
        sum +=scores[i]
    print(f'#{test_case} {sum}')
    