class Solution:
    def isValid(self, s: str) -> bool:

        # this will remember the opening brackets we see.
        stack = []

        # this tells us which opening bracket matches each closing bracket.
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        # go through each character in the string.
        for c in s:

            # if it's an opening bracket
            if c == "(" or c == "[" or c == "{":
                # remember it.
                stack.append(c)

            # ellse it's a closing bracket.
            else:

                #if there are no opening brackets to match it
                if len(stack) == 0:
                    return False

                #get the last opening bracket we saw.
                top = stack.pop()

                # if they don't match
                if top != pairs[c]:
                    return False

        # if there are no unmatched opening brackets left
        # the string is valid.
        return len(stack) == 0