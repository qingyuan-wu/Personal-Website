### Valid Sodoku
Approach: create a set. The set stores 3 things:
* Has the number num appeared in row i? Store as: (i, num)
* Has the number num appeared in column j? Store as: (num, j)
* Has the number num appeared in sub-square (i//3,j//3)? Store as: (i//3, j//3, num)

Iterate through the Sodoku and check these three things for each iteration. If none are found, then add these three things using set.add((i, num))...

The description is pretty much the pseudocode, but here's the Python solution nonetheless:

```python
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        found = set()
        # i is row number, j is column number
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    # if board[i][j] in i-th row, j-th column, or (i,j)-th square:
                    # note board[i][j] is a string
                    if (i, board[i][j]) in found or (board[i][j], j) in found or (i//3,j//3, board[i][j]) in found:
                        return False
                    found.add((i, board[i][j]))
                    found.add((board[i][j], j))
                    found.add((i//3,j//3, board[i][j])) 
        return True
```


### Search a 2D Matrix
A matrix is sorted, search for a number target and return T/F.

Treat this as a binary search problem. Pretend the matrix is flattened to a long list and set low, high, mid

Then to actually access the element, do `matrix[mid//n][mid%n]` (matrix is m by n).

Literally just standard binary search.

### Merge Sorted Array
Note: must be done in place, where nums1 contains extra space at the end (pre-filled with 0's).

Start from end and work your way to the front. Pretty much the standard merge function used in merge sort but in reverse.

Note that a collision would never occur because the end of nums1 have exactly len(nums2) 0's.

The last two lines just ensure that if nums2 didn't finish adding, add all of it (because by now all of nums1 has been added).

```python
# The key is to work from the end to the front
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=m-1,n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -=1
            k -= 1
            
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]
```

### Max Contiguous Subarray
### Best Time to Buy and Sell Stock

These are all DP-type problems. You don't even need extra memory! (No need to create a new list). 

There are two things you should store and update for each iteration: a `max_so_far` variable that stores the max contiguous subarray if you were to start at any point prior and **end at the current index, non-inclusive!**. If this max_so_far variable is negative, you don't want to include this in your subarray. Your max subarray would just start at the current index and end here. 

The second variable to track is `prev_max`. This is more straightforward: this variable stores subarray sum you've found so far.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_so_far asks: what would be our max if our subarray had to end at the current index, starting anywhere prior?
        max_so_far = nums[0]

        # prev_max asks: what's the max sum found so far, until the current index?
        prev_max = max_so_far
        for num in nums[1:]:
            if max_so_far > 0:
                max_so_far += num
            else:
                max_so_far = num
            prev_max = max(prev_max, max_so_far)
            
        return prev_max
```


### BST - convert to increasing tree (897)
Given the `root` of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Solution: we must use in-order traversal. For every subtree, append the left node, the root, and then the right node. Initialize by creating a node `ans=self.cur=TreeNode(None)`. From my understanding, creating `self.cur` is like creating a global variable that can be accessed in the inorder inner function. However, I tried creating a variable merely named `cur` and passing that in as a second argument in the inorder function, but this only gives the right half of the desired tree. I cannot figure out why.

The sandwiched part between the two inorder recursive calls is always where the magic happens. Here, we're appending the current node to cur.right and traversing right once (to make sure cur is always at the tip of the tree).

```python
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = self.cur.right
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
```

### Valid Anagram (242)
Check if two strings are anagrams of e/o. Return T/F

The trivial solution would be to sort the two list(str) and compare them. The more efficient way is to create two size 26 arrays to store the occurance of each Engligh letter for each string. Use ord(char) - ord('a') for indexing. This way 'a' is at index 0, 'z' is a index 25.

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        l1 = [0]*26
        l2 = [0]*26
        for i in range(len(s)):
            l1[ord(s[i]) - ord('a')] += 1
            l2[ord(t[i]) - ord('a')] += 1
            
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
            
        return True
```

### 334. Increasing Triplet Subsequence (medium)
Given unsorted array, return True if 3 elements (not necessarily consecutive) are increasing.

Here's my code:
```python
def increasingTriplet(self, nums: List[int]) -> bool:
    smallest=streak2= float('inf') # smallest is the min elem so far
        # streak2 is the value of the second element of 2 increasing elements exist
    
    for i in range(len(nums)):
        if nums[i] > streak2:
            return True
        if nums[i] > smallest:
            streak2 = min(streak2, nums[i])
        else: #nums[i] <= smallest
            smallest = nums[i]
            
    return False
```

Every loop, we first check to see if we get a number bigger than a streak a 2, if yes we can immediately return, because we have the situation `2......6......9 => True`. 

Then we check to see we can potentially update `streak2`. This happens when we have a scenario like: `2........6.......4`, where we can **completely** forget about 6 (since 4 is smaller than 6 and larger than min, or 2).

Finally, the number must be the potential start of another streak because it's smaller than the previous min. This situation is like `2.....6.....-5`. We still want to store `streak2` because whenever we get a number > 6 we return True, but storing -5 is also important because we can potentially start a new, better streak2 like `-5.....-3`.

### 435. Non-overlapping Intervals (medium)
We have a bunch of intervals, non-sorted, in the form of `[[a,b], [c,d], [e,f]...]`. The question asks us to return how many intervals we need to remove (minimum) to make all remaining intervals non-overlapping.

There are two approaches to this, both involving first sorting the list of intervals.

**Method 1**: sorting by end time. Do it like this: `sorted(intervals, key=lambda x: x[1])`. Then we can be greedy

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    end_bound = float('-inf')
    count = 0
    # Method 1: sort by the end time, when in conflict, always remove the one with the later end time.
    for start, end in sorted(intervals, key= lambda x: x[1]):
        if start >= end_bound:
            # no need to remove, simply update end_bound
            end_bound = end
        else:
            count += 1
            
    return count
```

**Method 2**: sorting by start time `intervals.sort()` will suffice. Here when in conflict, we can choose which one to remove (we always remove the one with the later end time, greedy again).
```python
    intervals.sort()
    remove = 0
    upper_bound = intervals[0][1] # must *clear* this value to be non-overlapping
    
    for start, end in intervals[1:]:                
        if start < upper_bound: # will need to remove
            remove += 1
            # always remove the one with the higher upper bound - greedy
            upper_bound = min(upper_bound, end)            
        else: # no need to remove
            upper_bound = end
        
    return remove
```

### 59. Spiral Matrix II (medium)
The solution (I did not come up with) I found is super cool. But first the question - super straight forward - output a matrix spiralling in from the [0,0] position. Input is `n` we want to generate an n-by-n matrix with entries from 1 to n**2. The code will speak for itself.

```python
def generateMatrix(self, n: int) -> List[List[int]]:
    # pre-fill n by n matrix with zeros
    res = [[0]*n for i in range(n)]
    i=j=0 # i = up/down, j = left/right
    di,dj=0,1 # +di => down, +dj => right
    for cur in range(1, n**2+1):
        res[i][j] = cur
        
        # this is sooo cool: the %n makes sure index is in bounds, i+di and j+dj simulates the next step. This line is saying if the next step reaches a non-zero number (already been set), we need to turn around
        if res[(i+di)%n][(j+dj)%n]:
            # this is also cool - this comes from observing the x and y turn pattern
            di, dj = dj, -di
           
        i += di
        j += dj
    
    return res
```

### 238. Product of Array Except Itself (medium)
Can't use division. We want to output an array. The key here is for every element of `arr`, its result is the successive multiplications of all elements left of it, multipled by the successive multiplications of all elements right of it. In fact, if we reversed the first two lines with the last two lines of the for loop, the output array should be all the same number - `prod(nums)` in particular.

This solution isn't easy to think of and is rather unintuitive imo. But just think like this maybe: everytime we always set the arr value *before* we multiply by the element (last two lines of for loop). Therefore, the nums elemenet itself is never included.


```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    # [2,3,4,5] - input
    # [60,40,30,24] - output
    arr = [1]*len(nums)
    left=right=1
    
    for i in range(len(nums)):
        arr[i] *= left
        arr[-i-1] *= right

        left *= nums[i]
        right *= nums[-i-1]
        
    return arr
```

### 409. Longest Palindrome (easy)
Common technique to sort strings: `"".join(sorted(string))`.