'''
separate into two array
one for letters and one for numbers
put numbers aside
in letter array
[m,a,n,o,b,c]
[a,m,n,o,b,c]
[a,m,n,,o]
TC: O(n.m Logn) 
Let N be the number of logs in the list and
M be the maximum length of a single log.
Sc = O(N.M)

'''
class Solution:
    def reorderLogFiles(self, logs):
        num_logs = []
        let_logs = []
        for l in logs:
            arr = l.split(" ")
            try:
                val = int(arr[1])
                num_logs.append(l)
            except:
                let_logs.append(arr)
        let_logs.sort(key=lambda x:x[0]) #first sort by identifiers 
        let_logs.sort(key=lambda x:x[1:])#now finalize the sort by remaining values
        i=0
        while(i<len(let_logs)):
            logs[i] = " ".join(let_logs[i])
            i+=1
        logs[i:] = num_logs
        return logs
    
class Main:
    result = Solution()
    print(result.reorderLogFiles())