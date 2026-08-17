import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        collection = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in collection:
                return [collection[complement], i]

            collection[nums[i]] = i
        return []

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    # logger.info(solution.twoSum(nums=nums, target=target))
    print(solution.twoSum(nums=nums, target=target))