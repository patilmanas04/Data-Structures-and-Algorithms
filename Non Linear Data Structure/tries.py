class Node:
  def __init__(self, val):
    self.val = val
    self.children = {}
    self.EOS = False
  
  def __str__(self):
    return f"value={self.val}"

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

  def end_of_prefix(self, node: Node, prefix: str, index: int, prefix_len: int):
    if index>=prefix_len:
      return node
    
    char = prefix[index]
    child_node = node.children.get(char)

    if child_node:
      return self.end_of_prefix(child_node, prefix, index+1, prefix_len)
    
    return child_node

  def auto_complete(self, prefix: str):
    search_node = self.end_of_prefix(self.root, prefix, 0, len(prefix))
    if not search_node: return []

    search_results = []
    def auto_complete_search(search_node: Node, current_string: str):
      if search_node.EOS: search_results.append(current_string)

      for child_node in search_node.children.values():
        auto_complete_search(child_node, current_string+  child_node.val)

    auto_complete_search(search_node, prefix)
    return search_results

trie = Trie()

# A curated dataset to test deep branches, subsets, and outliers
word_dataset = [
  # The 'car' branch (expanding on your originals)
  "car", "card", "cardboard", "care", "career", "careful", 
  "carpet", "carpool", "carrot", "carry", "cart", "carton",
  
  # The 'app' branch (Testing heavy subsets)
  "app", "apple", "application", "apply", "apparel", 
  "apparent", "apparatus", "appease", "append", "appendix",
  
  # The 'pro' branch (Testing long similar words)
  "pro", "program", "programmer", "programming", "progress", 
  "project", "projector", "protect", "protein", "protest",
  
  # The 'inter' branch
  "interact", "interest", "interesting", "internal", 
  "international", "internet", "interpret", "interrupt",
  
  # Short branches and random outliers
  "bat", "batch", "batter", "battery", "battle", "battalion",
  "cat", "catch", "category", "caterpillar",
  "dog", "dodge", "dogma",
  "hello", "help", "helmet",
  "zebra", "zero", "zephyr",
  "xylophone", "yak"
]

trie = Trie()

for word in word_dataset:
    trie.insert(word)

print("--- Autocomplete Tests ---")

print("\nPrefix 'car':")
print(trie.auto_complete("car"))

print("\nPrefix 'care':")
print(trie.auto_complete("care"))

print("\nPrefix 'progr':")
print(trie.auto_complete("progr"))

print("\nPrefix 'xylo':")
print(trie.auto_complete("xylo"))

print("\nPrefix 'zulu':")
print(trie.auto_complete("zulu"))

print("\nPrefix 'inter':")
print(trie.auto_complete("inter"))