nums = [2, 7, 11, 15]
target = 9

for num in range(len(nums)):
    for i in range(num + 1, len(nums)):
        if nums[num] + nums[i] == target:
            print([num],[i])