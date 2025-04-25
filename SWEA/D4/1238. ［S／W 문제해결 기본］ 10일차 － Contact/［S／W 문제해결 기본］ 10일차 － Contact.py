from collections import defaultdict
from collections import deque
for test_case in range(1, 11):
    data_len ,start = map(int,input().split())
    d = defaultdict(list)
    visited = dict()
    data = list(map(int,input().split()))
    ans = 0
    # 연락 그래프 dict로 정리 -> from : [to,to,to] 형식
    for i in range(0,len(data),2):
        k = data[i]
        v = data[i+1]
        d[k].append(v)
    # BFS
    q = deque()
    q.append((start,0)) # 시작점, depth초기값
    visited[start] = 0
    while q:
        n, depth = q.popleft()
        depth+=1
        for num in d[n]: # 다음 depth 연락
            if num not in visited.keys():
                q.append((num,depth))
                visited[num] = depth
        
    max_depth = max(visited.values())
    for key in visited.keys():
        if visited[key] == max_depth and key > ans:
            ans = key
    print("#" + str(test_case) + " " + str(ans))         
    
        
            
            
        

