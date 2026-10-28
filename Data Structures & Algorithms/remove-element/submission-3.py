class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N=len(nums)
        i=0
        j=N-1
        k=N
        while i<=j:
            while 0<j<N and nums[j]==val:
                print("while", j)
                j-=1
                k-=1
            if i<=j and nums[i]==val:
                print('val found')
                print(i,j)
                nums[i], nums[j]=nums[j], nums[i]
                i+=1
                j-=1
                k-=1
                
            else:
                print('valid int')
                i+=1
            print(nums)

        return k
        