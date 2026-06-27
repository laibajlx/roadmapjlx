class Solution:
   def hasDuplicate(self, nums: List[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


#create that hashset 
#then go thru every value in the input arr nums
#before you add evry value to hashset, (you must do this to hashet)
#check if n is a dupocate by checking if it's in hashet, then return true bcuz we ofund duplciation
#if doesn't contsain duplicate, add that value, iterate thru the arr of nums, then loop will exit
# return false becuz we did not find any duplicates in array

# your sticky notes (empty at start)
# go through each number
# already wrote this number down?
#  yes → duplicate found!
# no → write it down, move on
# checked everything, no duplicates
