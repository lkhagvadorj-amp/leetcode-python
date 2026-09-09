from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        max_strength = 0

        for i in range(n):
            for j in range(i + 1, n):
                g = gcd(nums[i], nums[j])
                strength = (nums[i] * nums[j]) // (g * g)
                max_strength = max(max_strength, strength)

        return max_strength

if __name__ == "__main__":
    nums = [2, 3, 5]
    solution = Solution()
    answer = solution.maxPairStrength(nums=nums)
    print(answer)