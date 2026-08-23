class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]

    solution = Solution()
    print(solution.removeDuplicates(nums=nums))