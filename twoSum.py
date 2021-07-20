class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums),1):
                if(nums[i]+nums[j]==target):
                    return [i,j]
           
s = Solution()
s.twoSum([2,7,11,15], 9)
s.twoSum([3,2,4], 6)
s.twoSum([3,3],6)