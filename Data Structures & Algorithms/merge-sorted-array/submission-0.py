class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        last = m+n-1

        j=m-1
        k=n-1
        i=0

        while k>=0:

            if j>=0 and nums1[j]>nums2[k]:
                nums1[last]=nums1[j]
                j-=1
            else:
                nums1[last]=nums2[k]
                k-=1

            last-=1


        