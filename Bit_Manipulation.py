class Solution(object):
    #Given an integer n, return true if it is a power of two.
      #Otherwise, return false.
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        a = 1
        while a < n:
            a = a << 1
            if a == n:
                return True
        return False
    #Write a function that takes an unsigned integer and returns
      #the number of '1' bits it has (also known as the Hamming weight).
    def hammingWeight(self, n):
        a = 1
        count = 0
        while a <= n:
            if a & n != 0:
                count += 1          
            a = a << 1

        return count

Sol = Solution()

num = 42

print("Is {n} power of two? {ans}.".format(n = num, ans = Sol.isPowerOfTwo(num)))

print(f"The Hamming weigth of {num} is {Sol.hammingWeight(num)}.")
