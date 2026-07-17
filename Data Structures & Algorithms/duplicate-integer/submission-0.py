class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = set()
        for i in nums:
            if i in isDuplicate:
                return True
            else:
                isDuplicate.add(i)
        return False