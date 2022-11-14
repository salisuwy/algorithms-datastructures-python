from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def inorder(self, node=None, root=False):
        if root and node is None:
            node = self.root
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def preorder(self, node=None, root=False):
        if root and node is None:
            node = self.root
        if node is None:
            return
        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def postorder(self, node=None, root=False):
        if root and node is None:
            node = self.root
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")
        
    def level_order(self, node=None):
        if node is None:
            node = self.root
        
        if node is not None:
            queue = deque()
            level = 0
            queue.append((node, level))

            while len(queue) > 0:
                new_node, new_level = queue.popleft()
                
                for i in range(new_level):
                    print("   ", end="")
                print(new_node.data)
                if new_node.left is not None:
                    queue.append((new_node.left, new_level+1))
                if new_node.right is not None:
                    queue.append((new_node.right, new_level+1))



    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if node.data == data:
            return node
        elif node.data > data:
            node.left = self._insert(node.left, data)
            return node
        else:
            node.right = self._insert(node.right, data)
            return node

    def remove(self, data):
        if self.root is None:
            print("The tree is empty")
        else:
            self.root = self._remove(self.root, data)
        
    def _remove(self, node, data):
        if node is None:
            return None
        if node.data > data:
            node.left = self._remove(node.left, data)
            return node
        elif node.data < data:
            node.right = self._remove(node.right, data)
            return node
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self.min(node.right)
                node.data = min_node.data
                node.right = self._remove(node.right, min_node.data)
                return node

    def search(self, data):
        if self.root is None:
            print("Empty tree")
            return False
        node = self.root
        while True:
            if node is None:
                return False
            
            if node.data == data:
                return True
            elif node.data > data:
                node = node.left
            else:
                node = node.right


    def min(self, node=None, root=False):
        if root and node is None:
            node = self.root
        if node is None:
            return None
        min_node = node
        while min_node.left is not None:
            min_node = min_node.left
        return min_node

    def max(self, node=None, root=False):
        if root and node is None:
            node = self.root
        if node is None:
            return None
        max_node = node
        while max_node.right is not None:
            max_node = max_node.right
        return max_node


if __name__ == "__main__":
    bst = BST()

    print(bst.search(30))

    bst.insert(50)
    bst.insert(30)
    bst.insert(11)
    bst.insert(43)
    bst.insert(57)
    bst.insert(6)
    bst.insert(13)
    bst.insert(40)

    bst.remove(30)

    print("Pre-order: ", end="   ")
    bst.preorder(root=True)
    print("")

    print("In-order: ", end="   ")
    bst.inorder(root=True)
    print("")

    print("Post-order: ", end="   ")
    bst.postorder(root=True)
    print("")

    print("Level-order: ", end="\n")
    bst.level_order()
    print("")

    print("min: ", bst.min(root=True).data)
    print("max: ", bst.max(root=True).data)

    print(bst.search(30))
    print(bst.search(2))
    print(bst.search(11))
    print(bst.search(59))