class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        matching_bracket = {"]": "[", ")": "(", "}": "{"}
        for i in s:
            if i in ["(", "{", "["]:
                stack.append(i)
            elif i in [")", "}", "]"]:
                print(matching_bracket[i])
                if stack and stack[-1] == matching_bracket[i]:
                    stack.pop()
                else:
                    return False

        return not stack
