class Solution:
    def minOperations(self, nums: list[int], target_sum: int) -> int:
        # Generate all possible (value, cost) pairs for each number
        possibilities = []
        for num in nums:
            possible = {}

            # Try multiplying k times, then dividing m times
            for mult in range(30):  # 2^30 > 10^9
                mult_val = num << mult  # num * 2^mult
                if mult_val > target_sum * 100:
                    break

                div_val = mult_val
                for div in range(mult + 30):  # Can divide after multiplying
                    if div_val == 0:
                        break
                    cost = mult + div
                    if div_val not in possible or possible[div_val] > cost:
                        possible[div_val] = cost
                    div_val >>= 1  # div_val //= 2

            possibilities.append(possible)

        # DP: minimum cost to achieve each sum
        dp = {0: 0}

        for possible in possibilities:
            new_dp = dp.copy()  # Keep all previous sums (not using this number)

            for current_sum, current_cost in dp.items():
                for value, value_cost in possible.items():
                    new_sum = current_sum + value
                    if new_sum <= target_sum:
                        new_cost = current_cost + value_cost
                        if new_sum not in new_dp or new_dp[new_sum] > new_cost:
                            new_dp[new_sum] = new_cost

            dp = new_dp

        return dp.get(target_sum, -1)

if __name__ == "__main__":
    nums = [10, 2]
    target_sum = 13

    solution = Solution()
    answer = solution.minOperations(nums=nums, target_sum=target_sum)
    print(answer)  # Expected: 3