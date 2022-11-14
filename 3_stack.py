class Stack:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def traverse(self):
        for item in self.items:
            print(item, end=" ")
        print("")

    def push(self, data):
        self.size += 1
        self.items.append(data)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            item = self.items.pop()
            return item
        else:
            raise Exception("Stack empty exception")

    def peek(self):
        if self.size > 0:
            return self.items[-1]
        return None


if __name__ == "__main__":
    s = Stack()
    s.push(20)
    s.push(30)
    s.traverse()
    print(s.peek())
    s.pop()
    s.traverse()