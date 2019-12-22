# My version Runtime 804 ms Memory 14.7 MB
def twoSum(nums, target):
    for index, num in enumerate(nums):
        diff = target - num
        # "if" consume more time 
        if diff in nums:
            diff_index = nums.index(diff)
            if diff_index != index:
                return [index, diff_index]

# other version Runtime 36ms Memory 14.5 MB
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    x = [2*nums[i] - target for i in range(len(nums))]
    for i in range(len(x)):
        neg = -1 * x[i]
        if neg in dic:
            return [dic[neg], i]
        else:
            dic[x[i]] = i

nums = [2, 7, 11, 15]
target = 9
twoSum(nums,target)
