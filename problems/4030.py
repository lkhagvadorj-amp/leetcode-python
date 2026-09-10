class Solution:
    def convert_binary(self, string: str) -> str:
        return "".join(format(ord(char), '08b') for char in string)

    def isPalindromic(self, s: str) -> bool:
        s_binary = self.convert_binary(s)
        left = 0
        right = len(s_binary) - 1

        while left < right:
            if s_binary[left] != s_binary[right]:
                return False
            left+=1
            right-=1

        return True

if __name__ == "__main__":
    s = "ff"

    solution = Solution()
    answer = solution.isPalindromic(s=s)
    # answer = solution.convert_binary(string=s)
    print(answer)