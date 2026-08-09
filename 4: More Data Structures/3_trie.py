class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes.
        self.isEnd = False  # Flag to represent end of a word.

class Solution:
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
        current_node.isEnd = True

    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node.children:
                return False
            else:
                current_node = current_node.children[word[i]]
        if current_node.isEnd:
            return True
        else:
            return False

    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in current_node.children:
                return False
            else:
                current_node = current_node.children[prefix[i]]
        return True