class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique=1

        i=0
        j=0

        while j<len(nums):
            if nums[j]==nums[i]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
                unique+=1
            # print(nums)
        return unique

        
        

        