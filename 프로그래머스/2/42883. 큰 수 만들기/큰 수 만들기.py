def solution(number, k):
    stack = []
    size = len(number)
    return_size = size - k
    for i,n in enumerate(number): # 10^6
        # stack.pop 한뒤에 새로 넣어도 자리수 문제없을 조건
        while stack and n > stack[-1] and size - i > return_size - len(stack):
            stack.pop()
        if len(stack) < return_size: # stack의 길이 제한
            stack.append(n)
    
    return "".join(stack)

solution("654321", 1)