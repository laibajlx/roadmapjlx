class Solution:
   def hasDuplicate(self, nums: List[int]) -> bool:
       seen = {}


       for num in nums:
           if num in seen:
               return True


           seen[num] = True


       return False


# your sticky notes (empty at start)
# go through each number
# already wrote this number down?
#  yes → duplicate found!
# no → write it down, move on
# checked everything, no duplicates
