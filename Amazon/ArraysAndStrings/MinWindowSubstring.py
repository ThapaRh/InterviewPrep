class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
        
        use the sliding window approach
        i will create dictionary to store char and counts of t
        and I will have a counter to see if we have found all characters of t in s
        2 pointers to go thru s, 
        new_dict for keeping tack of elements that s_dict had
        updaing count if t_dict[elem] == s_dict[elem]
        and once our count == unique elements: 
        resizing the window, if counter goes down we move right pointer to get counter up
        
        
        TC: O(s+m)
        SC: O(s)
        
        '''
        t_dict = {}
        s_dict = {}
        for element in t:
            if element in t_dict:
                t_dict[element]+=1
            else:
                t_dict[element] = 1
                s_dict[element] = 0
        i = 0
        j = 0
        if len(s)<len(t): #dont forget this line
            return ""
        count_match = 0
        min_length = len(s)+1
        final = ""
        unique_elements = len(t_dict)
        #loop for window
        while(j<len(s)):
            if s[j] in s_dict:
                s_dict[s[j]]+=1
                if s_dict[s[j]] == t_dict[s[j]]:
                    count_match += 1
            while count_match == unique_elements:
                new_length = j-i+1
                if new_length<min_length:
                    min_length = new_length
                    final = s[i:j+1]
                if i<=j and s[i] in s_dict: #i<=j this specific line of code, dont forget this
                    s_dict[s[i]]-=1
                    if s_dict[s[i]]<t_dict[s[i]]:
                        count_match-=1
                i+=1
            j+=1
        return final
