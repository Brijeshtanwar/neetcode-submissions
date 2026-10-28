class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        idx=0
        min_len = len(strs[0])
        for i in range(len(strs)):
            min_len=min(len(strs[i]), min_len)

        for i in range(min_len):
            j=0
            while j<len(strs)-1:
                # print(strs[j][i], strs[j+1][i])
                if strs[j][i]==strs[j+1][i]:
                    j+=1
                else:
                    return strs[0][:idx]
            idx+=1
        return strs[0][:idx]
        