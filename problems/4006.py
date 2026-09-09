class Solution:
    def countValidPrefixes(self, s: str) -> int:
        count = 0
        zeros = 0
        ones = 0

        for char in s:
            if char == '0':
                zeros += 1
            else:
                ones += 1

            # Valid if counts differ by at most 1
            if abs(zeros - ones) <= 1:
                count += 1

        return count

if __name__ == "__main__":
    s = "101"

    solution = Solution()
    answer = solution.countValidPrefixes(s)
    print(answer)
