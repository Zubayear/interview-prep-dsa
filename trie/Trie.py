class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        """
            [\0]
            /
           [] empty map
        """
        for char in word:
            if char not in current_node.children:
                """
                    [\0]
                    /
                   [a]
                   /
                  []  
                """
                current_node.children[char] = TrieNode()
            # move the current_node to empty dict
            current_node = current_node.children[char]
        # make the last node terminal
        current_node.end_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.end_word

    def starts_with(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

    def get_word(self, prefix):
        current_node = self.root
        word = []
        for char in prefix:
            if char not in current_node.children:
                return word
            current_node = current_node.children[char]
        # starts with found
        self._get_all_words(current_node, prefix, word)
        return word

    def _get_all_words(self, node, prefix, word):
        if node.end_word:
            # found the word so add it to result
            word.append(prefix)

        for char in node.children:
            # have to iterate the hashmap of p i.e. app[l,a]
            # we'll iterate through [l,a] to find words
            self._get_all_words(node.children[char], prefix + char, word)
