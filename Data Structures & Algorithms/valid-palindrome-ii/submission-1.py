class Solution:
    def pal(self, s):
        i=0
        j=len(s)-1
        while i<=j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        k=0
        i=0
        j=len(s)-1
        p_1=True
        p_2=True

        while i<=j and k<2:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                print(s[i:j+1])
                k+=1
                l_1=i+1
                r_1=j
                l_2=i
                r_2=j-1
                
                p_1 = self.pal(s[l_1:r_1+1])
                p_2 = self.pal(s[l_2:r_2+1])

                break
        

        print(k, p_1, p_2)
        if k <2 and (p_1 or p_2):
            return True
        else:
            return False
                
