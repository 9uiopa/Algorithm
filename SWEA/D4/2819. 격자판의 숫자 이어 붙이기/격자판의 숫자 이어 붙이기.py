T = int(input())
def dfs(r,c,t,num):
    curr = num+board[r][c]
    if t ==6:
        num_set.add(curr)
        return
    
    for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
        nr, nc = r + dr, c+dc
        if 0<=nr<4 and 0<=nc<4:
            dfs(nr, nc, t+1, curr)
        
for test_case in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]
    num_set = set()
    for i in range(4):
        for j in range(4):
            dfs(i,j,0,"")
    print("#" + str(test_case) + " " +str(len(num_set)))
        
