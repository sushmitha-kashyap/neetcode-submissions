class Solution:
    def hasDuplicate(self, num: List[int]) -> bool:
        num.sort()
        for i in range(len(num)-1):
                if num[i] == num[i+1]:
                    return True
        return False
 