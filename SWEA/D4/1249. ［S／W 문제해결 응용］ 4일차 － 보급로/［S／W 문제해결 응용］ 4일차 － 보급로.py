import heapq

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int,input())) for _ in range(n)]
    pq = []
    costs = [[9999]*n for _ in range(n)] # sys.maxsize 대체
    heapq.heappush(pq, (0,0,0)) # (time, r, c)
    costs[0][0] = 0
    ans = 0
    
    # 다익스트라
    while pq:
        times, r, c = heapq.heappop(pq)
        if r == n-1 and c == n-1:
            ans = times
            break
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr = r + dr
            nc = c + dc
            if (0<=nr<n) and (0<=nc<n) :
                next_times = times + graph[nr][nc]
                if next_times<costs[nr][nc] :
                    heapq.heappush(pq, (next_times, nr, nc))
                    costs[nr][nc] = next_times
    print("#" + str(test_case) + " " + str(ans))
                
                
                
        
        
    
    