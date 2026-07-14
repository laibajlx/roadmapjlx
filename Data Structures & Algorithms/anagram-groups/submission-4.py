class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # create an empty dict that will eventually looks like line 25

        for word in strs: #go thru the list one word at a time, first loop act, then pots, then tops...
            key = ''.join(sorted(word))  #word = "eat" sorted() does not retrun string it retunrs list so ['a', 'e', 't']
            # '' means put nothing in between letts and .join combines ['a', 'e', 't'] to "aet"
            #now key = "aet"

            if key not in groups: #if key is not in groups
                groups[key] = [] #checks whether sorted word(key) alr exists in dict, If it doesn't, Python creates a new empty list ([]) for that key so there is a place to store all the words that belong to that anagram group.

            groups[key].append(word) #adds a word to that list.
        return list(groups.values()) #gets all the lists of grouped anagrams from the dictionary, converts them into a regular list, and returns that final list as the answer.
        
    
#strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#map = {}

#"eat" -> sorted "aet" -> map["aet"] = ["eat"]
#"tea" -> sorted "aet" -> map["aet"] = ["eat", "tea"]
#"tan" -> sorted "ant" -> map["ant"] = ["tan"]
#"ate" -> sorted "aet" -> map["aet"] = ["eat", "tea", "ate"]
#"nat" -> sorted "ant" -> map["ant"] = ["tan", "nat"]
#"bat" -> sorted "abt" -> map["abt"] = ["bat"]

# {
#  "aet": ["eat", "tea", "ate"],
#  "ant": ["tan", "nat"],
# "abt": ["bat"]
# }