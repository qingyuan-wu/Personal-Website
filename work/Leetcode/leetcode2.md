### 230 K-th Smallest Element in BST
* This question is quite trickyyy
* A similar (harder) version of this problem is Leetcode 426 (see below)
* Steps:
  * Do inorder traversal
  * Every time you reach the smallest element, subtract 1 from k
  * If you reach k == 0, you can set the res and return

```python
    def KthSmallest(root, k):
        res = None
        def inorder(node):
            nonlocal res, k
            if node is None: return
            
            # go all the way left to get to the smallest
            inorder(node.left)
            
            # reached the smallest
            k -= 1
            if k == 0:
                res = node.val
                return
            
            # go one right, but then all the way left again
            inorder(node.right)
            
        inorder(root)
        return res
```

### 426 Convert BST to Doubly LL
* This question took me probably 3-5 hours to do in total...
* Recall the inorder traversal of a BST tree is sorted
* The very basic way to do the problem is to flatten the BST tree to a list of nodes using inorder traversal, then link them:

```python
def treeToDoublyList1(root):
    if root is None: return

    def build_list(node):
        if node is None:
            return []
        return build_list(node.left) + [node] + build_list(node.right)
    sorted_tree = build_list(root)
    for i in range(len(sorted_tree)):
        sorted_tree[i].left = sorted_tree[i-1]
    return sorted_tree[0] 
```
* Time: O(n), Space: O(n)
* This solution is good enough to pass, but not good enough to look cool and doesn't test your understanding of recursion
* Approach 2 involves recursively using inorder traversal to build the tree
* After calling build_list(node.left) recursively, you will reach the leftmost leaf of tree (smallest)
* From here, you set smallest to be that node
* For each recursive call, there's also a `cur_largest` variable, storing the max you've encountered so far 
* Every time the new node you encounter is one larger than cur_largest (because you're doing inorder traversal)
* This allows you to link the current node and cur_largest in the `else` block
* Before returning the smallest element, don't forget to link the smallest with the largest!

```python
def treeToDoublyList2(root):
        if root is None: return
        smallest = None
        cur_largest = None

        def build_list(node):
            # allow us to modify smallest, cur_largest
            nonlocal smallest, cur_largest
            if node is None: return

            build_list(node.left)
            
            # now node is the smallest since node.left is None
            # smallest is the smallest element from the entire BST
            if smallest is None:
                # the current node is the global smallest elem
                smallest = node
            else:
                # somewhere in the tree
                node.left = cur_largest
                cur_largest.right = node
            # update cur_largest since node is larger
            cur_largest = node

            build_list(node.right)

        build_list(root)
        smallest.left = cur_largest
        cur_largest.right = smallest
        return smallest
```
Time: O(n), Space: O(h), h is the height of the tree

* you can do something similar using a stack (iteratively)
* Just note that the exit condition for your while loop should be `while stack or node`