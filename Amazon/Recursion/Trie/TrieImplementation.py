'''
Trie is a tree-like data structure that is used to store a dynamic set of strings, it is similar to a tree but instead of having left and right children, 
each node can have multiple children which is why we used key-value pair(dictionary in python) to store the children of the node.
First node is the root node, which is empty and does not contain any character.

It is particularly useful for tasks like autocomplete, spell checking, and IP routing.
This implementation provides basic functionalities of a Trie, including insertion, search, and deletion of words.

TC for search, insert and find_prefixes is all O(m) where m is the length of the word/prefix being searched/inserted.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_word = True
    
    def search(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.is_word
    
    def has_prefix(self,prefix):
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]
        return True
    
class Main:
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple")) #true
    print(trie.has_prefix("apple")) #true
    print(trie.search("app")) #false
    print(trie.has_prefix("app")) #true
    trie.insert("app")
    print(trie.search("app")) #true
    print(trie.has_prefix("app")) #true