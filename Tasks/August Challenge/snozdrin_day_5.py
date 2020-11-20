# https://leetcode.com/problems/implement-trie-prefix-tree/

# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = dict()

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         node = self.root
#         for char in word:
#             if char not in node:
#                 node[char] = dict()
#             node = node[char]
#         node["#"] = True

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         node = self.root
#         for char in word:
#             if char not in node:
#                 return False
#             node = node[char]
#         if node.get("#"):
#             return True
#         return False

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         node = self.root
#         for char in prefix:
#             if char not in node:
#                 return False
#             node = node[char]
#         return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("apple")
# print(obj.search("apple"))
# print(obj.search("app"))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3413/

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        current = self.trie
        for letter in word:
            current = current.setdefault(letter, {})
        current['_end_'] = word

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.recursive_search(word, len(word), self.trie)

    def recursive_search(self, word, length, node):

        # prevent value in '_end_' be treated as new child
        if type(node) is not dict:
            return False

        current = node
        for i in range(len(word)):
            letter = word[i]

            # once meet '.', do recursive search for all it's children
            if letter == '.':
                return any([self.recursive_search(word[i+1:], length, current[child]) for child in current])

            # prefix not match, return False directly
            if letter not in current:
                return False

            current = current[letter]

        # once it runs to this line, it means all explicit letters are matched
        # so we only have to check the target word's length is matched
        return len(current.get('_end_', '')) == length

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("at")
# obj.addWord("ad")
# print(obj.search("a"))
# print(obj.print_trie())
