class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count how many times each number appears
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1

        answer = []  # We eventually need to return a list

        # Find the largest count k times
        for i in range(k):

            largest_count = 0
            largest_num = None

            for num in count:
                if count[num] > largest_count:
                    largest_count = count[num]
                    largest_num = num

            answer.append(largest_num)
            del count[largest_num]

        return answer
 
#suppose we use ex1 nums = [1, 2, 2, 3, 3, 3]
#start with empty dictionary count = {}
#loop through each num start with 1 in this ex1
#if 1 not in count -> count[1] = 1 so it looks like 1:1 in hashmap
# next loop through is 2, if 2 not in count -> count [2]=1 so it looks like 2:1 in hashmap
# next loop through is 2, 2 IS in count! -> count [2] add 1. whats in count 2 right now the value is 1 so 1+1 =2
# then repeat!!

  
   # {
   # 1:1 -> number: frequency
   # 2:2
   # 3:3
   # }

        