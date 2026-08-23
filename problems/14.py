class Solution:
    def longestCommonPrefixTwoString(self, str_1: str, str_2: str) -> str:
        n = min(len(str_1), len(str_2))
        common_prefix = ""

        for i in range(n):
            if str_1[i] == str_2[i]:
                common_prefix += str_1[i]
            else:
                break

        return common_prefix

    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = strs[0]

        for s in strs[1:]:
            common_prefix = self.longestCommonPrefixTwoString(common_prefix, s)

        return common_prefix

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]

    solution = Solution()
    print(solution.longestCommonPrefix(strs=strs))