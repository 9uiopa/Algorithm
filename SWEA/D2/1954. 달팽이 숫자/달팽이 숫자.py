T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print("#" + str(test_case))
    snail = [[0]*n for _ in range(n)]
    val = 1
    r = c = 0
    snail[0][0] = 1
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    idx = 0
    while val < n*n:
        dr, dc = direction[idx]
        nr, nc = r + dr , c + dc
        if 0<=nr<n and 0<=nc<n and snail[nr][nc] == 0:
            val+=1
            snail[nr][nc] = val
            r = nr
            c = nc
        else:
            idx = (idx+1)%4
    for row in snail:
        print(" ".join(list(map(str, row))))

    
            
            
            
        
    
