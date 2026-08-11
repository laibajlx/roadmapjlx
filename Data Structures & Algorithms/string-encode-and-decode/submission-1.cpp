class Solution {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encoded;
        for (const string& s : strs) {
            // Prefix each string with its length followed by a delimiter '#'
            encoded += to_string(s.size()) + '#' + s;
        }
        return encoded;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> decoded;
        int i = 0;
        while (i < s.size()) {
            // Find the delimiter '#' to get the length
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int len = stoi(s.substr(i, j - i));
            // Extract the actual string of that length
            string str = s.substr(j + 1, len);
            decoded.push_back(str);
            // Move i to the start of the next length-prefixed string
            i = j + 1 + len;
        }
        return decoded;
    }
};