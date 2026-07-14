class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # create an empty dict that will eventually looks like

        for word in strs:
            key = ''.join(sorted(word)) 

            if key not in groups:
                groups[key] = []

            groups[key].append(word)
        return list(groups.values())
        
    
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