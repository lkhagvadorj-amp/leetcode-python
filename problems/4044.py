class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2
        score = 0

        # Calculate initial left_sum for rotation k=1: [nums[1], nums[2], ..., nums[n-1], nums[0]]
        left_sum = sum(nums[1:half+1])
        total = sum(nums)

        # Check all rotations
        for k in range(n):
            right_sum = total - left_sum
            if left_sum > right_sum:
                score += 1

            # Update left_sum for next rotation (k+1)
            # When moving from rotation k to k+1:
            # - Element at position (k+1) moves out of left half
            # - Element at position (k+1+half) % n moves into left half
            if k < n - 1:
                left_sum -= nums[(k + 1) % n]
                left_sum += nums[(k + 1 + half) % n]

        return score

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]

    solution = Solution()
    answer = solution.countGoodRotations(nums=nums)
    print(answer)