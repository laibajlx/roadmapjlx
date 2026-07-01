#include <vector>
#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        
        for (int num : nums) {
            // if the element is already in the set dup fd
            if (seen.find(num) != seen.end()) {
                return true;
            }
            // othrwsie insert the element into the set
            seen.insert(num);
        }
        
        return false;
    }
};
