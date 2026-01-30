class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        print(first)

        cur = ""
        res = ""
        for i in range(len(first)):
            cur += first[i]
            for word in strs:
                if not word.startswith(cur):
                    return res
            res += first[i]

        return res