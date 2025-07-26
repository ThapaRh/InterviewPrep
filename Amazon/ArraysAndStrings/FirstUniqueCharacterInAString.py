
'''
I can save it in a set 
come back iterate and find the first element in array which is also in set

TC: O(N) SC: O(N)
'''
def firstUniqChar(s: str) -> int:
        s_dict = {}
        for w in s:
            if w in s_dict:
                s_dict[w]+=1
            else:
                s_dict[w] = 1
        for i in range(len(s)):
            if s_dict[s[i]]==1:
                return i
        return -1
print(firstUniqChar("LLLovers"))
                
