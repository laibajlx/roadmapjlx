class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i in range(len(nums)):
           for j in range((i+1), len(nums)):
               if nums[i] + nums[j] == target:
                   return[i,j] 
# box 0    box 1    box 2    box 3
#  3        4         5        6
#first iteration j=1 -> checks if nums[0]+nums[1] == target
                                     # 3 + 4  = 7 YAY
                                     # return [i,j]
#if no, j=2 -> check if nums[0]+nums[2] == target
                        #    3 + 5 = 8 NOPE