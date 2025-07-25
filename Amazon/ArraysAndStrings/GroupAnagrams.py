class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Example 1:

        Input: strs = ["eat","tea","tan","ate","nat","bat"]

        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        
        plan is to sort strings and save it as a key in dictionary and append unsorted string as value if its sorted version exists in dictionary
        
        '''
        final_dict = {}
        for s in strs:
            new_s = "".join(sorted(s))
            if new_s in final_dict:
                final_dict[new_s].append(s)
            else:
                final_dict[new_s] = [s]
        return list(final_dict.values())
