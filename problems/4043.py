class Solution:
    def calculate_score(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                score+=1
        return score

    def countRotations(self, s: str, k: int) -> int:
        count = 0
        score = 0

        for i in range(len(s)):
            s_rotate = s[i+1:]+s[:i+1]
            score = self.calculate_score(s_rotate)
            if score == k:
                count+=1

        return count

if __name__ == "__main__":
    s = "aab"
    k = 1

    solution = Solution()
    answer = solution.countRotations(s=s, k=k)
    print(answer)