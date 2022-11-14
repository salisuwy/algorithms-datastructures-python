from collections import deque
from collections.abc import Hashable

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} - {self.value}"

class HashMap:
    def __init__(self, capacity=20):
        self.capacity = capacity
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
            
            print(index)
            for data_item in item:
                print(" ", data_item)


    def is_hashable(self, key):
        return isinstance(key, Hashable)

    def hash_item(self, item):
        return hash(item) % self.capacity    

    def add(self, key, value):
        if not self.is_hashable(key):
            raise Exception("Key mush be hashable")

        _key = self.hash_item(key)
        if self.buckets[_key] is None:
            self.buckets[_key] = deque()
        
        bucket_items = self.buckets[_key]
        for index, data_item in enumerate(bucket_items):
            if key == data_item.key:
                # print(f"Key present in hash table")
                bucket_items[index] = HashItem(key, value)
                return

        # print(f"New data entry in the hash table")
        self.size += 1
        data = HashItem(key, value)
        self.buckets[_key].append(data)


    def get(self, key):
        if not self.is_hashable(key):
            raise Exception("Key mush be hashable")

        _key = self.hash_item(key)
        if self.buckets[_key] is not None:
            bucket_items = self.buckets[_key]
            for data_item in bucket_items:
                if key == data_item.key:
                    return data_item.value
        return None

    def pop(self, key):
        if not self.is_hashable(key):
            raise Exception("Key mush be hashable")

        _key = self.hash_item(key)
        if self.buckets[_key] is None:
            return
        
        bucket_items = self.buckets[_key]
        for index, data_item in enumerate(bucket_items):
            if key == data_item.key:
                self.size -= 1
                del bucket_items[index]
                return

    def clear(self):
        self.size = 0
        self.buckets = [None] * self.capacity

if __name__ == "__main__":
    h = HashMap(capacity=10)
    h.add("Hello", "Hello")
    h["Hello"] = "Hi"
    h["Hello"] = 30
    h.add("Student", "Hello")
    h.add(23, 23)
    h.add("Tell them", "Tell them")
    h.add((2, "Uganda"), (2, "Uganda"))
    h.traverse(include_empty=True)
    print("size: ", h.size)
    h.pop("HelloCC")
    print("size: ", h.size)
    print(h["Hello"])
    print(h.get(23))
    print(h.get((2, "Africa")))
    print(h.get((2, "Uganda")))
    h.clear()
    print("size: ", h.size)
