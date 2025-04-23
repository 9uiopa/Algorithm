T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    origin = list(input().split())
    l = len(origin)
    half = 0
    half = int(l/2) + 1 if l%2==1 else int(l/2)
    d1 = origin[:half] 
    d2 = origin[half:]
    ans = []
    for i in range(half):
        ans.append(d1[i])
        if i == len(d2):
            break
        ans.append(d2[i])
    print("#" + str(test_case)+" " + " ".join(ans))