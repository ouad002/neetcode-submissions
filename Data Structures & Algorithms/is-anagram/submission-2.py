class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s_c= Counter(s)
            s_t= Counter(t)
            for char in s_c:
                if char not in s_t:
                    return False
                elif s_c[char]!=s_t[char]:
                    return False
            return True
        