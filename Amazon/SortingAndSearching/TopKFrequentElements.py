def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    '''
    i could 
    0 1 2 3 4 5 6 7
    [][][][][][][][]
    we can either use bucket sort or just sort the dictionary 
    bucket sort: O(n) TC
    Dict:O(nlogn) TC
    SC: O(n)
    '''
    dict = {}
    for n in nums:
        if n in dict:
            dict[n]+=1
        else:
            dict[n]=1
    count = [[] for i in range(len(nums)+1)]
    for key,value in dict.items():
        count[value].append(key)
    final = []
    for i in range(len(count)-1,-1,-1):
        for v in count[i]:
            final.append(v)
            k-=1
            if k==0:
                return final
    return final