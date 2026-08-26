class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
      
       # if lengths are different they can't be anagrams
       if len(s) != len(t):
           return False
       countS = {}
       countT = {}
       #count letters in both strings
       for i in range(len(s)):
           countS[s[i]] = countS.get(s[i], 0) + 1
           countT[t[i]] = countT.get(t[i], 0) + 1
       #compare the dictionaries
       return countS == countT
