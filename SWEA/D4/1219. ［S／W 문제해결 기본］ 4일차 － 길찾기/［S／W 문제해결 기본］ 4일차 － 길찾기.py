T = 10
def dfs(idx):
    global ans
    if idx == 99:
        ans = 1
    for i in graph[idx]:
        if i not in visited:
            visited.add(i)
            dfs(i)
            visited.remove(i)

for test_case in range(1, T + 1):
    t , road_num = map(int, input().split())
    input_list = list(map(int,input().split()))
    graph = [[]*100 for _ in range(100)]
    visited =set()
    ans = 0
    for i in range(len(input_list)):
        if i%2 ==1:
            graph[input_list[i-1]].append(input_list[i])            
    visited.add(0)
    dfs(0)
    print(f'#{t} {ans}')
        
    