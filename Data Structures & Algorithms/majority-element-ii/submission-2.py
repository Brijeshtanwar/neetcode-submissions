class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        freq=Counter(nums)

        res=[]

        for num in freq:
            if freq[num]>n//3:
                res.append(num)
        return res
        