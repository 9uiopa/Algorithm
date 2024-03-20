
def solution(k, dungeons):
    def dfs(dungeons, k, count):
        ans = count
        for i, dungeon in enumerate(dungeons):
            if k >= dungeon[0]:
                next_k = k - dungeon[1]  # 던전을 탐험한 후의 피로도 , k변수 새로 써야함
                next_dungeons = dungeons[:i] + dungeons[i+1:]  # 다음 던전들
                ans = max(dfs(next_dungeons, next_k, count + 1), ans)  # 탐험가능 던전의 최댓값
        return ans

    return dfs(dungeons, k, 0)