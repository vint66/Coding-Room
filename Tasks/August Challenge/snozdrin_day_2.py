# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3410/

class MyHashSet:

    def __init__(self, size=10000):
        self.size = size
        self.array = [set(),] * self.size

    def _hash(self, key: int):
        hash_code = key % self.size
        return hash_code

    def add(self, key: int) -> None:
        index = self._hash(key)
        try:
            self.array[index].add(key)
        except:
            pass

    def remove(self, key: int) -> None:
        index = self._hash(key)
        try:
            self.array[index].remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.array[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
