#Given two strings s1 and s2, return true if s2 contains a permutation of s1,
#or false otherwise.

#In other words, return true if one of s1's permutations is the substring of s2.

class Solution(object):
    def checkInclusion(self, s1, s2):
        d1 = dict([(character,0) for character in string.ascii_lowercase])
        d2 = dict([(character,0) for character in string.ascii_lowercase])
        def hash(d0, s0):
            for _ in range(len(s0)):
                d0[s0[_]]+= 1
            
        l1 = list(s1)
        hash(d1, l1)

        l2 = list(s2)
        n1, n2 = len(l1), len(l2)        
        l2_ = l2[0:n1]
        hash(d2, l2_)
        if d1 == d2:
            return True

        if n1 > n2:
            return False
        
        for _ in range(1, n2 - n1+1):
            d2[l2[_-1]] -= 1
            d2[l2[_+n1 - 1]] += 1
            #print(d2)
            if d1 == d2:
                return True
        return False
