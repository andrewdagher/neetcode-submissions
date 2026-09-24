class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for i in range(len(nums)):
            if nums[i] in numbers:
                return True
            numbers.add(nums[i])
        return False