def solution(sizes):
    large = []
    small = []
        
    for list in sizes:
        list.sort()
        large.append(list[0])
        small.append(list[1])
    
    return max(large) * max(small)