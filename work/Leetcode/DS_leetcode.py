class Node:
    # linked list
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)

class Tree:
    # binary tree
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str(self):
        return str(self.value)

def reverseLL(head):
    if head.next == None:
        return
    cur = head.next
    while cur.next != None:
        # swap cur with cur.next
        # temp = cur.next
        # temptemp = head.next
        # head.next = temp
        # cur.next = cur.next.next
        # temp.next = temptemp

        temp = head.next
        head.next = cur.next
        cur.next = cur.next.next
        head.next.next = temp

def printLL(head):
    while head != None:
        print(head, end=" => ")
        head = head.next

    print("END")

def printReverseLL(head):
    s = ''
    while head != None:
        s = str(head.value) + ' => ' + s
        head = head.next

    s += "END"
    print(s)

def revNodes(cur):
    # reverse cur.next and cur.next.next
    if cur == None or cur.next == None or cur.next.next == None:
        # make sure a swap is necessary
        return False
    n = cur.next # next node
    nn = cur.next.next # next next node
    cur.next = nn
    n.next = nn.next
    nn.next = n
    return True


def reverseTree(head):
    if head == None:
        return
    head.left, head.right = head.right, head.left
    reverseTree(head.left)
    reverseTree(head.right)

def printTree(head):
    if head == None:
        return
    printTree(head.left)
    print(head.value, end=' ')
    printTree(head.right)

def treeList(head):
    if head == None:
        return []
    return treeList(head.left) + [head.value] + treeList(head.right)

HEAD = Node('start')
a = Node(5)
b = Node(6)
c = Node(7)
d = Node(8)
e = Node(9)
HEAD.next = a
a.next = b
b.next = c
c.next = d
d.next = e

printLL(HEAD)
reverseLL(HEAD)
printLL(HEAD)

a = Tree('a')
b = Tree('b')
c = Tree('c')
d = Tree('d')
e = Tree('e')
f = Tree('f')
g = Tree('g')
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g
printTree(a)
reverseTree(a)
printTree(a)

print(treeList(a))
def intersect(nums1, nums2):
    res = []
    # nlog(n) to sort
    nums1.sort()
    nums2.sort()

    # log(n) to find
    def binarySearch(num, nums):
        low, high = 0 , len(nums)-1
        mid = (low+high)//2
        # binary search code
        while low < high:
            if num < nums[mid]:
                high = mid
            elif num > nums[mid]:
                low = mid + 1
            else:
                break
            mid = (low+high)//2
        if nums[mid] == num:
            low = mid + 1
            nums = nums[low:]
            return True
        return False


    # want to binary search the longer array
    if len(nums1) < len(nums2):
        # n to loop, times log(n) to search
        for elem in nums1:
            if binarySearch(elem, nums2):
                res.append(elem)
    else:
        for elem in nums2:
            if binarySearch(elem, nums1):
                res.append(elem)

    return res


l1 = [1,2,2,1]
l2 = [2,2]
print(intersect(l1, l2))


def matrixReshape(mat, r, c):
    m = len(mat)
    n = len(mat[0])
    if m*n != r*c:
        return mat

    res = []
    # initialize to be 0's
    for i in range(r):
        res.append([0]*c)
    a=b=0   # a=row, b=col
    for i in range(r):
        for j in range(c):
            if b == n-1:
                a += 1
                b = 0
            else:
                b += 1
            res[i][j] = mat[a][b]

    return res

matrixReshape([[1,2],[3,4]], 1, 4)
