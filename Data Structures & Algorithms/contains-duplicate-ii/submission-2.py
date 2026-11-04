class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        i=0

        while i<n:
            j=i+1
            print(i,j)

            while j<i+k+1:
                # print('nums', nums[i], nums[j])
                if j<n and nums[i]==nums[j] and abs(i-j)<=k:
                    return True
                else:
                    j+=1
            i+=1

        return False
        