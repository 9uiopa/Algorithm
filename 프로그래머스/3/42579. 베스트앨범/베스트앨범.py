from collections import defaultdict
def solution(genres, plays):
    answer = []
    plays_per_genres = defaultdict(int)
    
    for i, play in enumerate(plays):
        plays_per_genres[genres[i]] += play 
    g = [t[0] for t in sorted(plays_per_genres.items(),key=lambda x:x[1], reverse = True)]
    
    for genre in g:
        plays_list = []
        for i,num in enumerate(plays):
            if genre == genres[i]:
                plays_list.append((num,i))
        temp = sorted(plays_list,key=lambda x: (-x[0], x[1]))
        answer.append(temp[0][1])
        if len(temp)>1:
            answer.append(temp[1][1])
    
    return answer