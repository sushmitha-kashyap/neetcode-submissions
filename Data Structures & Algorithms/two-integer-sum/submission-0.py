class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i,num in enumerate(nums):
            complement = target - num
            if complement in num_dict and num_dict[complement] != i:
                return [num_dict[complement],i]
            num_dict[num] = i
        return []