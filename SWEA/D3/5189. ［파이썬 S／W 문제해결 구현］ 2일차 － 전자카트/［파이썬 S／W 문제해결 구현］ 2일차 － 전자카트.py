T = int(input())
def dfs(start, end, cost, visited):
    global min_cost
    cost+= board[start][end]
    if cost >= min_cost: # 탐색 중지
        return
    if len(visited) == n-1: # 탐색 완료
        min_cost = min(cost+board[end][0], min_cost)
        return
    for i in range(1, n): # 다음 장소 방문
        if i not in visited:
            visited.add(i)
            dfs(end, i, cost, visited)
            visited.remove(i)

for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    min_cost = 1001 # 조건상 가능한 최대 cost +1
    dfs(0,0,0,set())
    print("#" + str(test_case) + " " + str(min_cost))
    