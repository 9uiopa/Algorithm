from collections import deque

def solution(priorities, location):
    ans = 0
    q = deque([(i,x) for i,x in enumerate(priorities)])
    
    while q:
        process = q.popleft()
        ok = True
        for p in q:
            if p[1]> process[1]:
                q.append(process)
                ok = False
                break
        if ok:
            ans += 1
            if process[0]==location:
                return ans
            
        

        
        
    
    
 