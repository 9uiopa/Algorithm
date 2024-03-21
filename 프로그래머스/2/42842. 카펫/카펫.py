def solution(brown, yellow):
    s = (brown-4)/2
    for num in range(1, int(s/2)+1):
        h = num # yellow의 높이
        w = s - h #yellow의 너비
        if w*h == yellow:
            return [w+2,h+2]
    