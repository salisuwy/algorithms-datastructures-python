from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVLBST:
    def __init__(self):
        self.root = None
    
    def clear(self):
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
        
        if node.data > data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        node.height = self.height(node)
        balance_factor = self.balance_node(node)

        if balance_factor > 1:      # L-Rotate
            if node.left.data > data:    # LL-Imbalance  -> Right Rotate
                node = self.rotate_right(node)
            else:                   # LR-Imbalance  -> Left->Right Rotate
                node.left = self.rotate_left(node.left)
                node = node.rotate_right(node)           
        elif balance_factor < -1:   # R-Rotate
            if node.right.data < data:    # RR-Imbalance  -> Left Rotate
                node = self.rotate_left(node)
            else:                   # RL-Imbalance  -> Right->Left Rotate
                node.right = self.rotate_right(node.right)
                node = node.rotate_left(node)           
            
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
            
        elif node.data < data:
            node.right = self._remove(node.right, data)
            
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
        
        if node is None:
            return None
        
        node.height = self.height(node)
        balance_factor = self.balance_node(node)

        if balance_factor > 1:     # L-Imbalance
            if self.balance_node(node.left) >= 0:  # LL Imbalance - Right Rotate
                node = self.rotate_right(node)
            else:                                   # LR Imbalance - Left->Right Rotate
                node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)
        elif balance_factor < -1:   # R-Imbalance
            if self.balance_node(node.right) <= 0:  # RR Imbalance - Left Rotate
                node = self.rotate_left(node)
            else:                                   # LR Imbalance - Left->Right Rotate
                node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)

        return node


    def search(self, data):
        node = self.get_node(data)
        if node is None:
            return False
        else:
            return True


    def get_node(self, data):
        if self.root is None:
            print("Tree is empty")
            return None

        node = self.root
        while True:
            if node is None:
                return None
            
            if node.data == data:
                return node
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

    def height(self, node):
        if node is None:
            return -1
        
        height_left = self.height(node.left)
        height_right = self.height(node.right)
        return 1 + max(height_left, height_right)

    def balance_node(self, node):
        balance_factor = self.height(node.left) - self.height(node.right)
        # print(f"Node: {node.data}  ==> {balance_factor}")
        return balance_factor


    """ 
            ROTATE RIGHT

        A                     B
       / \                   / \
      B   x     ==>>        C   A
     / \                       / \
    C   y                     y   x

    """
    def rotate_right(self, node):
        new_root = node.left                      # B
        node_new_left = new_root.right            # y
        node.left = node_new_left                 # A.left = y
        new_root.right = node                     # B.right = A
        node.height = self.height(node)           # A.height = ?   
        new_root.height = self.height(new_root)   # B.height = ? 
        return new_root


    """ 
            ROTATE LEFT

        A                     B
       / \                   / \
      x   B     ==>>        A   C
         / \               / \
        y   C             x   y       

    """
    def rotate_left(self, node):
        new_root = node.right                      # B
        node_new_right = new_root.left             # y
        node.right = node_new_right                # A.right = y
        new_root.left = node                       # B.left = A
        node.height = self.height(node)            # A.height = ?   
        new_root.height = self.height(new_root)    # B.height = ? 
        return new_root


if __name__ == "__main__":
    avl = AVLBST()

    print(avl.search(30))

    avl.insert(50)
    avl.insert(30)
    avl.insert(11)
    avl.insert(43)
    avl.insert(57)
    avl.insert(6)
    avl.insert(13)
    avl.insert(40)

    # left imbalance
    avl.insert(5)
    avl.insert(4)
    avl.insert(3)
    avl.insert(2)
    avl.insert(1)
    avl.insert(0)

    # right imbalance 
    avl.insert(58)
    avl.insert(59)
    avl.insert(60)
    avl.insert(61)
    avl.insert(62)
    avl.insert(63)

    # remove nodes
    avl.remove(0)
    avl.remove(2)
    avl.remove(5)
    avl.remove(4)
    avl.remove(11)

    # avl.clear()

    print("Pre-order (AVL): ", end="   ")
    avl.preorder(root=True)
    print("")

    print("In-order (AVL): ", end="   ")
    avl.inorder(root=True)
    print("")

    print("Post-order (AVL): ", end="   ")
    avl.postorder(root=True)
    print("")

    print("Level-order (AVL): ", end="\n")
    avl.level_order()
    print("")

    print("min: ", avl.min(root=True).data)
    print("max: ", avl.max(root=True).data)

    print(avl.search(30))
    print(avl.search(2))
    print(avl.search(11))
    print(avl.search(59))