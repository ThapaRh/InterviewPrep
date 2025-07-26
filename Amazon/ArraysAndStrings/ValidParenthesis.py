class Solution:
    def isValid(self, s: str) -> bool:
        '''
        saving the brackets type in dictionary
        putting open brackets in stack
        when closed is found we look at the top of stack and it has to be open for that close
        TC: O(N)
        SC:O(N)
        '''
        dict = {")":"(",
                "}":"{",
                "]":"["}
        stack = []
        for bracket in s:
            if bracket not in dict:
                stack.append(bracket)
            else:
                if stack:
                    openB =  stack.pop()
                    if openB != dict[bracket]:
                        return False
                else:
                    return False
        if stack:
            return False
        return True

class Main:
    result = Solution()
    print(result.isValid("(]"))