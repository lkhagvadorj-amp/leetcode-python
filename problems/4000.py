class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > n * 9:
            return -1

        answer = [0]*n

        for i in range(n):
            digit = min(9,s)
            answer[i] = digit
            s -= digit
            if s == 0:
                break

        return int("".join(str(i) for i in answer))

if __name__ == "__main__":
    n = 2
    s = 9

    solution = Solution()
    answer = solution.largestInteger(n=n, s=s)
    print(answer) # expected 90