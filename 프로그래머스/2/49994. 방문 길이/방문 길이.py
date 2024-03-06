def solution(dirs): 
    answer = 0
    visited = set()
    x = 0
    y = 0
    
    for c in dirs: # n = 500
        if c == "U" and y+1<6:
            if (x,y,x,y+1) not in visited and (x,y+1,x,y) not in visited: 
                visited.add((x,y,x,y+1))
            y+=1
        elif c == "D" and y-1>-6:
            if (x,y,x,y-1) not in visited and (x,y-1,x,y) not in visited: 
                visited.add((x,y,x,y-1))
            y-=1            
        elif c == "R" and x+1<6:
            if (x,y,x+1,y) not in visited and (x+1,y,x,y) not in visited: 
                visited.add((x,y,x+1,y))
            x+=1            
        elif c == "L" and x-1>-6:
            if (x,y,x-1,y) not in visited and (x-1,y,x,y) not in visited: 
                visited.add((x,y,x-1,y))
            x-=1             
    print(visited)
    return len(visited)