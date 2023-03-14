class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: 
        if len(s) != len(t):
            return false

        d={}
        r=set()

        for i in range(len(s)):
            S=s[i]
            T=t[i]

            if S in d:
                if d[S] != T:
                    return False
            
            else:
                if T in r:
                    return False

                d[S]=T
                r.add(T)

        return True


