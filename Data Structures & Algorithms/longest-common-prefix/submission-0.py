class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substring = strs[0]
        if len(strs) == 1:
            return substring


        for i in range(1, len(strs)):
            sub = ""
            for j in range(min(len(strs[i]), len(substring))):
                if strs[i][j] == substring[j]:
                    sub += strs[i][j]
                else:
                    break

            if len(sub) < len(substring):
                substring = sub
        return substring
                