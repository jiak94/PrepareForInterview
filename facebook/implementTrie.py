class TrieNode(object):
    def __init__(self, char):
        self.character = char
        self.children = dict()
        self.complete = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode("*")
    
    def insert(self, word):
        tmp = self.root
        for i in range(len(word)):
            if i == len(word) - 1:
                if word[i] in tmp.children:
                    tmp.children[word[i]].complete = True
                else:
                    new_node = TrieNode(word[i])
                    new_node.complete = True
                    tmp.children[word[i]] = new_node
                    return
            
            if word[i] in tmp.children:
                tmp = tmp.children[word[i]]
            else:
                new_node = TrieNode(word[i])
                tmp.children[word[i]] = new_node
                tmp = tmp.children[word[i]]

    def search(self, word):
        tmp = self.root
        for char in word:
            if char in tmp.children:
                tmp = tmp.children[char]
            else:
                return False
        return tmp.complete

    def startsWith(self, prefix):
        tmp = self.root
        for char in prefix:
            if char in tmp.children:
                tmp = tmp.children[char]
            else:
                return False
        return True