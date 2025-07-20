'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
We search for word in a grid of characters, where each character can be used only once in a word.
Tc: m*n* 4^(m*n)
SC: S
Where 
m is the number of rows, 
n is the number of columns, 
t is the maximum length of any word in the array 
words and 
s is the sum of the lengths of all the words.
'''
#follow up: how to remove elements from trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_word = True 
        
    def return_root(self):
        #returns the root of the trie
        return self.root
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        trie_root = trie.return_root()
        
        row = len(board)
        col = len(board[0])
        
        final = set()
        
        def search(r,c,node,word):
            #base case
            if node.is_word:
                final.add(word)
            if r>=row or c>=col or r<0 or c<0 or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r,c))
            #search for board[r][c] in trie_node
            if board[r][c] in node.children:
                search(r+1,c,node.children[board[r][c]],word+board[r][c])
                search(r-1,c,node.children[board[r][c]],word+board[r][c])
                search(r,c+1,node.children[board[r][c]],word+board[r][c])
                search(r,c-1,node.children[board[r][c]],word+board[r][c])
            visited.remove((r,c))
        
        for i in range(row):
            for j in range(col):
                visited = set()
                search(i,j,trie_root,"")
        return list(final)
                
