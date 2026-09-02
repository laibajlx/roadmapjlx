class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0

        while i < len(s):
            j = i

            # Find the #
            while s[j] != "#":
                j += 1

            # Get the length of the word
            length = int(s[i:j])

            # Move past the #
            j += 1

            # Get the word
            word = s[j:j + length]
            answer.append(word)

            # Move to the next encoded word
            i = j + length

        return answer