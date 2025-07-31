'''
topological sort
we need incoming nodes
incoming = [0 for i in range(n)]
course_graph = defaultdict(list)
[0,1]
1->0
b->a
iterate thru courses:
[a,b]
dict[b].append(a)
incoming[a]+=1

q= add eveything that has incoming 0
if q is empty:
return false 
while(q):
keep going over nodes and keeping track of how many nodes were popped

if all popped then it's possible else it's not  possible
TC: O(n+e)
SC = O(n)
'''
from collections import defaultdict,deque
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    incoming = [0 for i in range(numCourses)]
    course_graph = defaultdict(list)
    for [a,b] in prerequisites:
        course_graph[b].append(a)
        incoming[a]+=1
    q=deque([])
    for i in range(numCourses):
        if incoming[i] == 0:
            q.append(i)
    if not q:
        return False
    count = 0
    while(q):
        count+=1
        node = q.popleft()
        for n in course_graph[node]:
            incoming[n]-=1
            if incoming[n]==0:
                q.append(n)
    if count==numCourses:
        return True
    return False
        
    