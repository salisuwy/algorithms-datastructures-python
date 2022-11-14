from doubly_linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.items = LinkedList()
    
    def traverse(self):
        self.items.traverse()

    def push(self, data):
        self.items.insert_back(data)

    def pop(self):
        if self.items.size > 0:
            item = self.items.head.data
            self.items.remove_front()
            return item
        else:
            print("Empty queue")
    def peek(self):
        if self.items.size > 0:
            item = self.items.head.data
            return item
        else:
            print("Empty queue")

if __name__ == "__main__":
    s = Queue()
    s.push(20)
    s.push(30)
    # s.pop()
    s.traverse()
    print(s.peek())
    s.pop()
    s.traverse()