class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            
            node = node.children[c]

        node.end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, index):
            if index >= len(word):
                return node.end

            c = word[index]

            if c == '.':
                for childNode in node.children.values():
                    if dfs(childNode, index + 1):
                        return True

                return False

            if c not in node.children:
                return False
            
            return dfs(node.children[c], index + 1)

        return dfs(self.root, 0)
