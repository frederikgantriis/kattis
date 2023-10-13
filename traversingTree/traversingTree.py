preorder = map(int, input().split())

class Node:
    def __init__(self, right, left):
        self.right = right
        self.left = left
    
parentNode = None

for i in range(len(preorder)):
    if parentNode is None:
        parentNode = preorder[i]
        return 
    