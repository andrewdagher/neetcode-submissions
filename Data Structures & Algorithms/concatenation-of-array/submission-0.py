class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n = len(nums) - 1
        # ans = []
        # for i in range(2*(n+1)):
        #     ans.append(0)
        # for i in range(n+1):
        #     ans[i] = nums[i]
        # for i in range(n+1):
        #     ans[i + (n + 1)] = nums[i]
        # return ans

        ans = []
        n = len(nums)
        for i in range(n):
            ans.append(nums[i])
        for i in range(n):
            ans.append(nums[i])
        return ans