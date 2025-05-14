t = int(input())

for _ in range(t):
    length = int(input())
    nums = list(map(int, input().split()))
    
    nums.sort()  # Important to make adjacent diffs meaningful

    possible = True
    for i in range(1, length):
        if nums[i] - nums[i - 1] > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")
