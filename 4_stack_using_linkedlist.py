from 2_doubly_linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.items = LinkedList()
    
    def traverse(self):
        self.items.traverse()

    def push(self, data):
        self.items.insert_back(data)

    def pop(self):
        if self.items.size > 0:
            item = self.items.tail.data
            self.items.remove_back()
            return item
        else:
            print("Empty stack")
    def peek(self):
        if self.items.size > 0:
            item = self.items.tail.data
            return item
        else:
            print("Empty stack")

if __name__ == "__main__":
    s = Stack()
    s.push(20)
    s.push(30)
    # s.pop()
    s.traverse()
    print(s.peek())
    s.pop()
    s.traverse()