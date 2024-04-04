def solution(n, computers):
    result = 0
    visited = [0]*n
    
    def dfs(i):
        if visited[i] == 1 : # 이미 방문된 곳이면 종료
            return False
        visited[i]= 1 # 처음이면 방문한다.
        
        for j in range(n):
            if computers[i][j]==1 and visited[j]==0: # 연결되어있고, 방문하지 않았으면 방문
                dfs(j)
        return True
    
    for i in range(n):
        if dfs(i) == True:
            result += 1

    return result