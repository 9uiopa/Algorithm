import sys
def dfs(graph, visited, node):
    count = 1
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(graph, visited, neighbor)
    return count

def solution(n, wires):
    min_diff = sys.maxsize
    for i in range(len(wires)): # 전선 끊어진 모든 경우 
        # 전력망 그래프 생성
        graph = [[] for _ in range(n+1)] # 0 ~ n 까지 존재하도록
        for j, (a, b) in enumerate(wires):
            if i == j:
                continue  # 전선 끊기 처리 
            graph[a].append(b)
            graph[b].append(a)

        # 전력망을 두 개로 분할하여 송전탑 개수 계산
        visited = [False] * (n+1)
        count1 = dfs(graph, visited, wires[0][0])  # 첫 번째 전력망
        count2 = n - count1  # 두 번째 전력망

        # 송전탑 개수의 차이 계산하여 최소값 갱신
        diff = abs(count1 - count2)
        min_diff = min(min_diff, diff)

    return min_diff