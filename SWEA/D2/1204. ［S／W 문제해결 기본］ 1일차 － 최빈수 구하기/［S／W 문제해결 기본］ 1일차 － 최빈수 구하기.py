T = int(input())
for test_case in range(1, T + 1):
    t = int(input())
    nums = list(input().split())
    nums.sort()
    max_cnt = 0
    ans = 0
    cnt = 0
    for i, num in enumerate(nums):
        if i < 1 :
            cnt+=1
            max_cnt = cnt
            ans = num
            continue
            
        if nums[i-1] == num:
            cnt+=1
            if cnt>= max_cnt :
                max_cnt = cnt
                ans = num
        else :
            cnt = 1

    print("#"+ str(t) + " " + ans)