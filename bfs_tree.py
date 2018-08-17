"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import Queue

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    node_vals = []
    world = Queue.Queue()

    def traver(self):
        while(not self.world.empty()):
            (root, level) = self.world.get()
            print "Current:", root.val , level
            next_level = level + 1
            # out of length of list
            if next_level > len(self.node_vals) - 1:
                self.node_vals.append([])

            if root.left != None:
                self.world.put((root.left, next_level))
                self.node_vals[next_level].append(root.left.val)
            if root.right != None:
                self.world.put((root.right, next_level))
                self.node_vals[next_level].append(root.right.val)
        self.node_vals = self.node_vals[:-1]

    def levelOrder(self, root):
        if root is None:
            return []
        #
        self.node_vals = []
        self.world = Queue.Queue()
        self.world.put((root, 0))
        self.node_vals.append([root.val])
        self.traver()
        return self.node_vals
