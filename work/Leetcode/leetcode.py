class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        pali = s[0] # longest palindrome
        i = 0 # index
        L = len(s)
        while i+max_len < L:
            j = i + max_len + 1
            while j <= L:
                str = s[i:j]
                if str == str[::-1]:
                    pali = s[i:j]
                    max_len = j-i
                j += 1
            i += 1
        print(max_len)
        return pali

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        d = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        while num > 0:
            i = 0
            for value in values:
                if value <= num:
                    res += d[value]
                    num -= value
                    break
                else:
                    i += 1
            values = values[i:]

        return res

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10 == 0 and x != 0):
            return False

        secondHalfFlipped = 0

        while x > secondHalfFlipped:
            secondHalfFlipped = secondHalfFlipped * 10 + x%10
            x //= 10

        # 12321 -> 1232, 1 -> 123, 12, -> 12, 123
        # 1221 -> 122, 1 -> 12, 12

        return x == secondHalfFlipped or x == secondHalfFlipped//10

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        # make sure reversed number is in range [-2^31, 2^31-1]
        if x >= 0:
            while x > 0:
                res = 10*res + x%10
                x //= 10
                if res > 2**31 - 1:
                    return 0
            return res
        else: # x < 0
            x = -x
            while x > 0:
                res = 10*res + x%10
                x //= 10
                if res > 2**31:
                    return 0
            return -1*res

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'{':'}', '[':']', '(':')'}
        stack = []
        for char in s:
            if char in d:
                stack.append(char)
            elif len(stack) == 0 or d[stack.pop()] != char:
                return False

        return len(stack) == 0

s1= Solution()
print(s1.longestPalindrome("cbabc"))

t2 = Solution()
print(t2.intToRoman(20))


def Fib(n):
    res = "1"
    x = 1
    y = 1
    i = 0
    start = 0
    end = 10
    while i < n:
        res += str(y)
        x, y = y, x+y

        i += 1
        while end <= len(res):
            if isPrime(int(res[start:end])):
                return res[start:end]
            start += 1
            end += 1


    return None


def isPrime(N):
    i = 3
    if N%2 == 0 and N != 2:
        return False

    while i <= N**0.5:
        if N%i == 0:
            return False
        i += 2

    return True

# print(isPrime(11))
# print(Fib(19))

def firstNonRepeating(s):
    d = {}
    for i, c in enumerate(s):
        if d.get(c) == None:
            d[c] = i
        else:
            d[c] = -1

    cur_min = 100000
    for char in d.keys():
        if d[char] != -1 and d[char] < cur_min:
            cur_min = d[char]

    if cur_min == 100000:
        return '_'
    return cur_min

print(firstNonRepeating("bacdaefbdfec"))

class Rotate(object):
    def __init__(self, matrix):
        self.matrix = matrix
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # total_shift_steps = len - 1
        # down_shifts = j (0,1,2,3...)
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix)-i-1):

                right = len(matrix) - j - i- 1
                down = j-i
                # total = len(matrix)-1-2*i
                # print(right,down)
                # print(matrix[i][j], matrix[i+down][j+right], matrix[i+down+right][j+right-down], matrix[i+right][j-down])
                matrix[i][j], matrix[i+down][j+right], matrix[i+down+right][j+right-down], matrix[i+right][j-down] = matrix[i+right][j-down], matrix[i][j], matrix[i+down][j+right], matrix[i+down+right][j+right-down]

M = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
a = Rotate(M)
a.rotate(M)
print(M)

class Solution2(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        row = [1,1]
        prev_temp = row[1]
        for i in range(rowIndex-1):
            for j in range(1, len(row)):
                temp = row[j-1]
                row[j] = row[j-1]+prev_temp
                prev_temp = temp
            row.append(1)

        return row

a=Solution2()
print(a.getRow(5))

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        minus = False
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            minus = True
        dividend = bin(abs(dividend))
        divisor = bin(abs(divisor))

        if int(divisor,2) > int(dividend,2):
            return 0

        res = "0b"
        i = len(divisor)
        if dividend[:i] < divisor:
            i += 1

        res += "1"
        cur = bin(int(dividend[:i], 2) - int(divisor, 2))
        while i < len(dividend):
            cur += dividend[i]
            if int(cur,2) >= int(divisor,2):
                res += "1"
                cur = bin(int(cur, 2) - int(divisor, 2))
            else:
                res += "0"
            i += 1
        return res


    def permute(self, nums):
        import math
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 1:
            res.append(nums)
            return res

        for i in range(math.factorial(len(nums)-1)):
            L = [nums[0]]
            L.extend(permute(nums[1:]))
            res.append(L)


        return res

# def permute( nums):
#     import math
#     """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#     """
#     res = []
#     if len(nums) == 1:
#         res.append(nums[0])
#         return res
#
#     for i in range(math.factorial(len(nums)-1)):
#         L = [nums[0]]
#         L.extend(permute(nums[1:]))
#         res.append(L)
#
#
#     return res
# print(permute([1,2,3,4]))
# # print(a.divide(2147483648, 1))
#
# import math
# print(math.factorial(5))

def find_lps(pattern):
    lps = [0]*len(pattern)
    j = 0
    add = 1
    for i in range(1, len(lps)):
        if pattern[i] == pattern[j]:

            lps[i] = add
            j += 1
            add += 1
        else:
            j = 0
            add = 1
            if pattern[i] == pattern[j]:
                lps[i] = add
                j += 1
                add += 1

    return lps
def match(string, pattern):
    # find first occurrance of pattern in string
    lps = find_lps(pattern)
    j = 0 # track pattern index
    i = 0 # track string index
    while i < len(string) and j < len(pattern):
        if string[i] != pattern[j]:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]


        else:
            j += 1
            i += 1


    if j == len(pattern):
        return i - j
    return -1


print(match("abcabababdbababc", "ababc"))

class Solution4:
    # dynamic programming: house robbing
    # store the data for the last 3 houses in a list. Note the prev house or outcome[2] cannot be robbed by rule. So rob either the house with one space or two space (note we don't rob the house with 3 space because then we just rob the house with one space + one space).
    # This solution takes constant space because we account for all the previously robbed data in outcome[0] and outcome[1]. Both of them are the max number of money received if they robbed up until and including that house.
    def rob(self, nums: List[int]) -> int:
        outcome = [0,0,nums[0]]
        for i in range(1, len(nums)):
            cur = max(outcome[0], outcome[1]) + nums[i]
            outcome[0], outcome[1], outcome[2] = outcome[1], outcome[2], cur

        return max(outcome[1],outcome[2])