class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        # 전위는 출력, 왼쪽, 오른쪽으로 순회
        print(node, end='') # 출력
        if not node.left == None : self.preorder(node.left) # 왼쪽
        if not node.right == None : self.preorder(node.right) # 오른쪽

    def inorder(self, node):
        # 중위는 왼쪽, 출력, 오른쪽으로 순회
        if not node.left == None : self.preorder(node.left) # 왼쪽
        print(node, end='') # 출력
        if not node.right == None : self.preorder(node.right) # 오른쪽

    def postorder(self, node):
        # 후위는 왼쪽, 오른쪽, 출력으로 순회
        if not node.left == None : self.preorder(node.left) # 왼쪽
        if not node.right == None : self.preorder(node.right) # 오른쪽
        print(node, end='') # 출력

    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node


a = [1,2,3,4,5,6,7]
node = []
for i in range(len(a)):
    node.append(Node(a[i]))

m_tree = BinaryTree()

for i in range(int(len(node)/ 2)):
    m_tree.makeRoot(node[i], node[i*2+1], node[i*2+2])

m_tree.preorder(m_tree.root)

m_tree.inorder(m_tree.root)

m_tree.postorder(m_tree.root)

m_tree