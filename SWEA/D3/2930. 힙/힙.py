import heapq
T = int(input())
for test_case in range(1, T + 1):
    pq = []
    n = int(input())
    ops = [list(map(int,input().split())) for _ in range(n)]
    result = []
    for op in ops:
        if len(op) == 2: # 연산1
            heapq.heappush(pq, op[1]*(-1))
        else: # 연산2
            if len(pq)>0:
                num = (-1)*(heapq.heappop(pq))
                result.append(num)
            else: result.append(-1)
    if len(result)>0:
    	ans = " ".join(map(str,result))
    else : ans = ""
    print(f'#{test_case} {ans}')
    