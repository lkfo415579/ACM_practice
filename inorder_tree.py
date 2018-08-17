class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    node_vals = []
    
    def traver(self, root):
        # write your code here
        if root == None:
            return
        # print "left", root.left, root.val
        self.traver(root.left)
        self.node_vals.append(root.val)
        self.traver(root.right)
        
    def inorderTraversal(self, root):
        self.node_vals = []
        self.traver(root)
        return self.node_vals
