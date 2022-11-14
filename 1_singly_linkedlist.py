class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data, end=" -> ")
            node = node.next
        print("$")
        return ""

    def traverse(self):
        print(self) 

    def is_empty(self):
        return self.size == 0   

    def insert_front(self, data):
        self.size += 1
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = self.head
            return
        temp.next = self.head
        self.head = temp

    def insert_rear(self, data):
        self.size += 1
        temp = Node(data)
        if self.tail is None:
            self.tail = temp
            self.head = self.tail
            return
        self.tail.next = temp
        self.tail = temp

    def insert_at(self, index, data):
        if index == 0:
            self.insert_front(data)
        elif index == self.size:
            self.insert_rear(data)
        elif index > self.size:
            raise Exception("Invalid index provided")
        else:  
            self.size += 1
            temp = Node(data)
            counter = 0
            node = self.head
          
            while counter < index - 1:
                node = node.next
                counter += 1
            
            temp.next = node.next
            node.next = temp

    def remove_at(self, index):
        if index >= self.size:
            raise Exception("Invalid index supplied")

        self.size -= 1
        if index == 0:
            if self.head is self.tail:
                self.tail = None
            self.head = self.head.next
        else:
            node = self.head
            while index > 1:
                index -= 1
                node = node.next
            if node.next is not None:
                 if node.next is self.tail:
                     self.tail = node                 
                 node.next = node.next.next
        
    def remove(self, data):
        if (self.head is not None) and (self.head.data == data):
            self.size -= 1
            if self.head is self.tail:
                self.tail = None
            self.head = self.head.next
            return

        node = self.head
        while node.next is not None:
            if node.next.data == data:
                self.size -= 1
                if node.next is self.tail:
                    self.tail = node
                node.next = node.next.next
                return
            
            node = node.next
        
        
if __name__ == "__main__":
    sll = SinglyLL()
    sll.insert_rear(20)
    sll.insert_rear(10)
    sll.insert_rear(2)
    sll.insert_rear(19)
    sll.traverse()
    sll.insert_front(12)
    sll.insert_at(0, 9)
    sll.traverse()
    sll.insert_at(5, 21)
    sll.traverse()
    sll.insert_at(2, 1)
    sll.traverse()
    print(sll.size)
    sll.insert_at(8, 11)
    sll.traverse()
    sll.remove_at(0)
    sll.traverse()
    sll.remove(21)
    sll.traverse()
    sll.remove_at(4)
    sll.traverse()
    sll.remove(99)
    sll.traverse()