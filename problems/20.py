class Solution:
    def isValid(self, s: str) -> bool:
        character_mapping = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for char in s:
            if char in character_mapping:
                # Opening bracket
                stack.append(char)
            else:
                # Closing bracket
                if not stack:
                    return False

                opening = stack.pop()

                if character_mapping[opening] != char:
                    return False

        return len(stack) == 0

if __name__ == "__main__":
    s = "()[]{}"

    solution = Solution()
    print(solution.isValid(s=s))