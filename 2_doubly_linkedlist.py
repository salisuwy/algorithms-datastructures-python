class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self, reversed=False):
        if reversed:
            node = self.tail
            while node is not None:
                print(node.data, end=" <=> ")
                node = node.prev
        else:
            node = self.head
            while node is not None:
                print(node.data, end=" <=> ")
                node = node.next
        print("")

    def insert_front(self, data):
        self.size += 1
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
            return
        self.head.prev = temp
        temp.next = self.head
        self.head = temp

    def insert_back(self, data):
        self.size += 1
        temp = Node(data)
        if self.tail is None:
            self.tail = temp
            self.head = temp
            return
        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp

    def insert_at(self, index, data):
        if index == 0:
            self.insert_front(data)
        elif index == self.size - 1:
            self.insert_back(data)
        elif index >= self.size:
            raise Exception("Index out of range error")
        else:
            self.size += 1
            node = self.head
            temp = Node(data)
            counter = 0
            while counter < index:
                node = node.next
                counter += 1
            prev = node.prev
            prev.next = temp
            temp.prev = prev
            temp.next = node
            node.prev = temp 

    def remove_front(self):
        if self.size > 0 and self.head is not Node:
            self.size -= 1
            if self.head is self.tail:
                self.tail = None
                self.head = None
                return
            next_node = self.head.next
            next_node.prev = None
            self.head.next = None
            self.head = next_node

    def remove_back(self):
        if self.size > 0 and self.tail is not Node:
            self.size -= 1
            if self.tail is self.head:
                self.tail = None
                self.head = None
                return
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail.prev = None
            self.tail = prev_node
            

    def remove_at(self, index):
        if index == 0:
            self.remove_front()
        elif index == self.size - 1:
            self.remove_back()
        elif index >= self.size:
            raise Exception("Index out of range error")
        else:
            self.size -= 1
            node = self.head
            counter = 0
            while counter < index:
                node = node.next
                counter += 1
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node

    def remove(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                self.size -= 1
                prev_node = node.prev
                next_node = node.next
                if node is self.head:
                    if self.head is self.tail:
                       self.head = None
                       self.tail = None
                    else: 
                        next_node.prev = None
                        self.head = next_node 
                elif node is self.tail:
                    prev_node.next = None
                    self.tail = prev_node
                else:
                    prev_node.next = next_node
                    next_node.prev = prev_node
                return True
            node = node.next
        return False

    def find(self, data):
        if self.size == 0:
            return False
        node = self.head
        while node is not None:
            if node.data == data:
                return True
            node = node.next
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_front(21)
    ll.insert_front(3)
    ll.insert_back(11)
    ll.insert_back(1)
    ll.traverse()
    ll.insert_at(0, 0)
    ll.traverse()
    ll.insert_at(3, 7)
    ll.traverse()
    ll.traverse(True)
    ll.insert_at(5, 9)
    ll.traverse()

    ll.remove_front()
    ll.traverse()
    ll.remove_back()
    ll.traverse()
    ll.remove(3)
    ll.traverse()
    ll.remove(1)
    ll.traverse()
    ll.traverse(reversed=True)

    ll.remove(7)
    ll.traverse()
    ll.traverse(reversed=True)