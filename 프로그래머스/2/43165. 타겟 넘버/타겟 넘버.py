def solution(numbers, target):
    answer = 0
    def dfs(index, sum):
        nonlocal answer
        if index == len(numbers):
            if sum == target :
                answer += 1
            return
        num = numbers[index]
        dfs(index + 1, sum + num)
        dfs(index + 1, sum - num)

    dfs(0, 0)
    return answer