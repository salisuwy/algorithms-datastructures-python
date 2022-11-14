from collections.abc import Hashable

class Empty:
    pass

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} - {self.value}"

class HashMap:
    def __init__(self, capacity=20, load_factor=0.80):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [None] * capacity

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def traverse(self, include_empty=False):
        for index, item in enumerate(self.buckets):
            if item is None:
                if include_empty:
                    print(index, item)
                continue
            
            print(index, item)     # repeatition. Can refactor line 28


    def is_hashable(self, key):
        return isinstance(key, Hashable)

    def hash_item(self, item):
        return hash(item) % self.capacity    

    def add(self, key, value):
        if not self.is_hashable(key):
            raise Exception("Key is not hashable")

        _key = self.hash_item(key)

        while True:
            item = self.buckets[_key]

            print(f"Loop: {_key} == {item}")

            if item is None or isinstance(item, Empty):
                print(f"New Entry - {item}")
                self.size += 1
                self.buckets[_key] = HashItem(key, value)
                self.balance_reharsh()
                return
            
            if key == item.key:
                print(f"Override - {item}")
                self.buckets[_key] = HashItem(key, value)
                return    

            _key = (_key + 1) % self.capacity
            print(f"Getting a new key - {_key}")
            

    def get(self, key):
        if not self.is_hashable(key):
            raise Exception("Key is not hashable")

        _key = self.hash_item(key)

        while True:
            item = self.buckets[_key]
            if item is None:
                return None
            
            if isinstance(item, HashItem) and key == item.key:
                return item.value   
            
            _key = (_key + 1) % self.capacity

    def remove(self, key):
        if not self.is_hashable(key):
            raise Exception("Key is not hashable")

        _key = self.hash_item(key)

        while True:
            item = self.buckets[_key]
            
            if item is None:
                print("No item found")
                return False
            
            if isinstance(item, HashItem) and item.key == key:
                self.buckets[_key] = Empty()
                self.size -= 1
                return True
            
            _key = (_key + 1) % self.capacity



    def balance_reharsh(self):
        balance_fact = self.size / self.capacity
        if balance_fact <= self.load_factor:
            return

        # reharsh
        new_capacity = self.capacity * 2
        new_map = HashMap(capacity=new_capacity)
        
        print(f"Rehashed from {self.capacity} to {new_capacity}")

        for item in self.buckets:
            if not (item is None or isinstance(item, Empty)):
                new_map.add(item.key, item.value)

        
        self.capacity = new_map.capacity
        self.size = new_map.size
        self.buckets = new_map.buckets


    def clear(self):
        self.size = 0
        self.buckets = [None] * self.capacity

if __name__ == "__main__":
    h = HashMap(capacity=2)
    h["name"] = "Salisu"
    h.traverse(include_empty=True)
    h.remove("name")
    h.traverse(include_empty=True)
    h["age"] = 32
    h.traverse(include_empty=True)
    h["name"] = "Salisu"
    h["bio"] = "Male and African"
    h.traverse(include_empty=True)
    h.add("Hello", "Hello")
    h["Hello"] = "Hi"
    h["Hello"] = 30
    h.add("Student", "Hello")
    h.add(23, 23)
    h.add("Tell them", "Tell them")
    h.add((2, "Uganda"), (2, "Uganda"))
    h.traverse(include_empty=True)

    print("***************")
    print("size: ", h.size)
    h.remove("Hello")
    print("size: ", h.size)
    h.traverse(include_empty=True)
    print("*******************")

    print(h["Hello"])
    print(h.get(23))
    print(h.get((2, "Africa")))
    print(h.get((2, "Uganda")))

    h.clear()
    print("size: ", h.size)
