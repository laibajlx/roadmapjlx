class Solution:
   def trap(self, height: List[int]) -> int:
       #if we go thru an arr of blocks, we can store water where there is a left side and right side so we need two ptrs, l at start, r which starts at the other end of arr
       #we're always able to store potentially up to the max heights so make two max trackers
       #step 3 make a total to store the water
       #step 4 move through the arr with a while loop
       #step 5 check which side is shorter
       #step 6 if current height beats 1Max, water runs down, so instead update lMax
       #step 6 otherwise add the diff to total
       #step 7 move left ptr inward
       l = 0
       r = len(height) - 1
       lMax = 0
       rMax = 0
       total = 0


       while l < r:


           if height[l] < height[r]:
               if height[l] > lMax:
                   lMax = height[l]
               else:
                   total = total + (lMax - height[l])
               l = l + 1


           else:
               if height[r] > rMax:
                   rMax = height[r]
               else:
                   total = total + (rMax - height[r])
               r = r - 1


       return total
