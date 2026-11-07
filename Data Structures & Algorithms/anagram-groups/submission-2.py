class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for str in strs :
            count = [0]*26
            for ch in str:
                count[ord(ch)-ord('a')]+=1
            if tuple(count) not in res :
                res[tuple(count)]=[str]
            else:
                res[tuple(count)].append(str)
        
        return list(res.values())