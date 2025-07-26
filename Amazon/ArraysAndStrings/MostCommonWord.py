'''
maxCount = 0
final = ""
convert banned to set for O(1) search
go thru the paragraph, build a word
if char is not alphabet then finish off the word formation
convert to lower case and
check to see if banned set has that word
no: add word to dict with count
if count>maxCount
update final and maxCount
        TC: O(N+M)
        SC:O(N+M)
'''

class Solution:
    def mostCommonWord(self, paragraph, banned):
        set_b = set(banned)
        dict_words = {}
        paragraph_l = paragraph.lower()
        paragraph_l+="."
        i = 0
        new_word = ""
        max_count = 0
        final = ""
        while(i<len(paragraph_l)):
            #building the word
            if paragraph_l[i].isalpha():
                new_word+=paragraph_l[i]
                i+=1
                continue
            else:
                if len(new_word)>0 and new_word not in set_b:
                    if new_word in dict_words:
                        dict_words[new_word]+=1
                    else:
                        dict_words[new_word] = 1
                    count = dict_words[new_word]
                    if count>max_count:
                        max_count = count
                        final = new_word
                new_word = ""
                i+=1
        return final
    
class Main:
    result = Solution()
    print(result.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))