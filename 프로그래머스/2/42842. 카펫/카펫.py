def solution(brown, yellow):
    sum = (brown-4)/2
    for num in range(1, int(sum/2)+1):
        h = num
        w = sum - h
        if w*h == yellow:
            return [w+2,h+2]
    