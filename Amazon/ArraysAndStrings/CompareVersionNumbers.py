class Solution:
    #note to myself: read the question carefully you lazy ass, try different examples before actually coding you bitch lol..sexy bitch tho haha..
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        j = 0
        
        ver1 = len(version1)
        ver2 = len(version2)
        
        while(i<ver1 and j<ver2):
            v1 =  0
            v2 = 0
            while(i<ver1):
                if version1[i]!=".":
                    v1 = v1*10+int(version1[i])
                    i+=1
                else:
                    i+=1
                    break
            while(j<ver2):
                if version2[j]!=".":
                    v2 = v2*10+int(version2[j])
                    j+=1
                else:
                    j+=1
                    break
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
            
        while(i<ver1):
            if version1[i]!="." and version1[i]!="0":
                return 1
            i+=1
        while(j<ver2):
            if version2[j]!="." and version2[j]!="0":
                return -1
            j+=1
        return 0
