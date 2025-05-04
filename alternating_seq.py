t = int(input())
n = int(input())
nums = list(map(int, input().split()))


sums = 0
i = 0
while i < n:

    if nums[i] > 0:
        element = nums[i]
        i +=1
        while i < n and nums[i] > 0:
            if nums[i] > element:
                element = nums[i]
            i+=1
        sums += element

    elif nums[i] < 0:   
        element = nums[i]
        i += 1
        while i < n and nums[i] < 0 :
            if nums[i] > element:
                element = nums[i]
            i += 1
        sums += element 
print(sums)
