from collections import defaultdict

class Node:
  def __init__(self, val):
    self.val = val
    self.children = defaultdict(Node)
    self.EOS = False

class Trie:
  def __init__(self):
    self.root = Node("")

  def insert(self, word):
    current = self.root

    for char in word:
      if char not in current.children:
        current.children[char] = Node(char)
      current = current.children[char]
    
    current.EOS = True

trie = Trie()

trie.insert("car")
trie.insert("carpet")
trie.insert("carpool")