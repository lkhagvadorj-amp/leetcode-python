class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        sum, pre = 0, "I"
        for c in s[::-1]:
            if symbol_mapping[c] < symbol_mapping[pre]:
                sum, pre = sum - symbol_mapping[c], c
            else:
                sum, pre = sum + symbol_mapping[c], c
        return sum

if __name__ == "__main__":
    s = "LVIII"

    solution = Solution()
    print(solution.romanToInt(s=s))