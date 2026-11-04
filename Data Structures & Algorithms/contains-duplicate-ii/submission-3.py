class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        i=0

        while i<n:
            j=i+1

            while j<i+k+1:
                if j<n and nums[i]==nums[j] and abs(i-j)<=k:
                    return True
                else:
                    j+=1
            i+=1

        return False
        