#Given an array of integers citations where citations[i]
#is the number of citations a researcher received for their ith paper, r
#eturn compute the researcher's h-index.

#According to the definition of h-index on Wikipedia:
#Ascientist has an index h if h of their n papers have atleast h citations each,
# and the other n − h papers have no more than h citations each.

#If there are several possible values for h,
#the maximum one is taken as the h-index.




class Solution(object):
    def hIndex(self, citations):
        N = len(citations)
        Counter = [0 for _ in range(N+1)]
        for cit in citations:
            if cit < N:
                Counter[cit] += 1
            else:
                Counter[N] += 1
        h_test = 0
        for _ in reversed(range(N+1)):
            h_test += Counter[_]
            if h_test >= _:
                return _
        return 0

S = Solution()
print("h-index = %i" %(S.hIndex([3,0,6,1,5])))
