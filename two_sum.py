# My version Runtime 804 ms Memory 14.7 MB
def twoSum(nums, target):
    for index, num in enumerate(nums):
        diff = target - num
        # "if" consume more time 
        if diff in nums:
            diff_index = nums.index(diff)
            if diff_index != index:
                return [index, diff_index]

# other version Runtime 36ms~52ms Memory 14.7 MB
def twoSum2(nums, target):
    # two number are the same 
    same_val = target / 2
    if nums.count(same_val) == 2:
        index_front = nums.index(same_val)
        index_end = nums.index(same_val, index_front + 1)
        return [index_front, index_end]
    # two number are not same 
    diff = [target - x for x in nums if x != (target/2)]
    elements = list(set(nums).intersection(set(diff)))
    return [nums.index(elements[0]),nums.index(elements[1])]

nums = [2, 7, 11, 15]
target = 9
twoSum(nums,target)
