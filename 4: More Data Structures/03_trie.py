"""
Design and implement a Trie (also known as a Prefix Tree). A trie is a tree-
like data structure that stores a dynamic set of strings, and is particularly 
useful for searching for words with a given prefix.

Implement the Solution class:

Solution() Initializes the object.
void insert(word) Inserts word into the trie, making it available for 
future searches.
bool search(word) Checks if the word exists in the trie.
bool starts_with(word) Checks if any word in the trie starts with the 
given prefix.

Example 1:
Input:
Trie operations: ["Trie", "insert", "search", "starts_with"]
Arguments: [[], ["apple"], ["apple"], ["app"]]
Expected Output: [-1, -1, 1, 1]
Justification: After inserting "apple", "apple" exists in the Trie. There is 
also a word that starts with "app", which is "apple".

Example 2:
Input:
Trie operations: ["Trie", "insert", "search", "starts_with", "search"]
Arguments: [[], ["banana"], ["apple"], ["ban"], ["banana"]]
Expected Output: [-1, -1, 0, 1, 1]
Justification: After inserting "banana", "apple" does not exist in the 
Trie but a word that starts with "ban", which is "banana", does exist.

Example 3:
Input:
Trie operations: ["Trie", "insert", "search", "starts_with", "starts_with"]
Arguments: [[], ["grape"], ["grape"], ["grap"], ["gr"]]
Expected Output: [-1, -1, 1, 1, 1]
Justification: After inserting "grape", "grape" exists in the Trie. There 
are words that start with "grap" and "gr", which is "grape".
"""

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes.
        self.is_end = False  # Flag to represent end of a word.

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        current_node = self.root
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                current_node.children[word[i]] = TrieNode()
                current_node = current_node.children[word[i]]
        current_node.is_end = True

    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node.children:
                return False
            else:
                current_node = current_node.children[word[i]]
        if current_node.is_end:
            return True
        else:
            return False

    # Returns if there is any word in the trie that starts with the given prefix.
    def starts_with(self, prefix: str) -> bool:
        current_node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in current_node.children:
                return False
            else:
                current_node = current_node.children[prefix[i]]
        return True

# Test:
def print_trie(node: TrieNode, prefix: str = "", char_label: str = "Root"):
    """
    Recursively prints a Trie structure with branch guides and word markers.
    """
    # Indicate if this node completes a word
    marker = " (★)" if node.is_end else ""
    print(f"{prefix}{char_label}{marker}")

    # Prepare prefix for child branches
    child_prefix = prefix + "    "
    
    # Sort children keys for consistent output
    items = sorted(node.children.items())
    
    for i, (char, child_node) in enumerate(items):
        is_last = (i == len(items) - 1)
        branch = "└── " if is_last else "├── "
        
        # If the child node has children of its own, format its branch
        print_trie(child_node, prefix + ("    " if is_last else "│   "), branch + char)

trie = Trie()
trie.insert('apple')
trie.insert('banana')
print(trie.search('apple'))
print(trie.search('app'))
print(trie.starts_with('app'))
print(trie.search('banana'))
print(trie.search('ban'))
print(trie.starts_with('ban'))
trie.insert('app')
print(trie.search('app'))
print_trie(trie.root)

