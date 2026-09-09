class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            #tac
            #cat -> 012 -> check how many times c has been seen:1+0
            #countS[s[0]] = 1
            #c:1-> nowrepeat all thru out
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT            