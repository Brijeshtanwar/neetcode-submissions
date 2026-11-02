class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=len(word1)

        l=0
        r=len(word2)

        res=""

        if j<=r:
            
            for idx in range(j):
                res+=word1[idx]
                res+=word2[idx]

            res=res+word2[idx+1:r+1]

        else:
            for idx in range(r):
                res+=word1[idx]
                res+=word2[idx]

            res=res+word1[idx+1:j+1]


        return res
    

        