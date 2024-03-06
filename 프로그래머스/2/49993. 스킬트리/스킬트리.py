from collections import deque # popleft 때문에
def solution(skill, skill_trees):
    answer = 0
    set_skill = set(skill)
    
    for skill_tree in skill_trees:
        q = deque(skill)
        valid = True
        for c in skill_tree:
            if c in set_skill: 
                if not q:
                    break
                if c==q[0]:
                    q.popleft()
                else:
                    valid = False
                    break
        if valid:
            answer+=1
    return answer