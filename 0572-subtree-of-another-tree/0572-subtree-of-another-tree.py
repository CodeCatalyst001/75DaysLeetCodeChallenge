# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        
        def serialize(node):
            if not node:
                return "#"
            return f",{node.val}" + serialize(node.left) + serialize(node.right)
        
        s = serialize(root)
        t = serialize(subRoot)
        
        return self.kmp(s, t)
    
    def kmp(self, text, pattern):
        lps = [0] * len(pattern)
        
        # Build LPS array
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
        
        # Search
        j = 0
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]
            if text[i] == pattern[j]:
                j += 1
                if j == len(pattern):
                    return True
        
        return False