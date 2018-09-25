"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        # fuck i know what 7 it saying now
        
        def build(start, end):
            if start > end:
                return None
            
            # find max
            p = start
            max_p = start
            for _ in nums[start:end]:
                if nums[max_p] < nums[p + 1]:
                    max_p = p + 1
                p += 1
            
            root = TreeNode(nums[max_p])
            root.left = build(start, max_p - 1)
            root.right = build(max_p + 1, end)
            return root
            
            
        root = build(0, len(nums) - 1)
        
        def dfs(root):
            if root == None:
                return
            print root.val
            dfs(root.left)
            dfs(root.right)
            
        # dfs(root)
        # print '-'
        # print root.left.val
        # print root.right.val
        
        def height(root, h):
            if root == None:
                return h
            h1 = height(root.left, h + 1)
            h2 = height(root.right, h + 1)
            return max(h1, h2)
                
            
        def travel(root, h, target_h):
            if root == None:
                if h == target_h:
                    print "#",
                return
            if h > target_h:
                return
            elif h == target_h:
                print root.val,
                
            travel(root.left, h + 1, target_h)
            travel(root.right, h + 1, target_h)
            
            
        # # travel(root)
        # H = height(root, 0)
        # for i in range(H):
        #     travel(root, 0, i)
        
        return root
