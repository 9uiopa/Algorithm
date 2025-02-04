def solution(A,B):
    t = len(A)
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(t):
        answer += A[i]* B[i]
    return answer