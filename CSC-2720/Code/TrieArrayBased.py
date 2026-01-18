class Trie:
    class Node:
        ALPHABET_SIZE = 26

        def __init__(self, value):
            self.value = value
            self.children = [None] * Trie.Node.ALPHABET_SIZE
            self.is_end_of_word = False

        def has_child(self, ch):
            return self.children[ord(ch) - ord("a")] is not None

        def has_children(self):
            for child in self.children:
                if child is not None:
                    return True
            return False

        def get_child(self, ch):
            return self.children[ord(ch) - ord("a")]

        def add_child(self, ch):
            self.children[ord(ch) - ord("a")] = Trie.Node(ch)

        def remove_child(self, ch):
            self.children[ord(ch) - ord("a")] = None

    def __init__(self):
        self.root = self.Node("")

    def insert(self, word):
        current = self.root
        for ch in word:
            if not current.has_child(ch):
                current.add_child(ch)
            current = current.get_child(ch)
        current.is_end_of_word = True

    def find(self, word):
        current = self.root
        for ch in word:
            if not current.has_child(ch):
                return False  # Word was not found
            current = current.get_child(ch)
        return current.is_end_of_word  # Return true if the word exists

    def remove(self, word):
        if word is None:
            return
        self._remove(self.root, word, 0)

    def _remove(self, node, word, idx):
        if idx == len(word):
            node.is_end_of_word = False
            return

        ch = word[idx]
        child = node.get_child(ch)

        if child is None:
            return

        self._remove(child, word, idx + 1)

        if not child.has_children() and not child.is_end_of_word:
            node.remove_child(ch)

    def words_with_prefix(self, prefix):
        list_of_words = []
        last_node = self.find_last_node_of(prefix)

        if last_node:
            self.collect_words(last_node, prefix, list_of_words)

        return list_of_words

    def find_last_node_of(self, prefix):
        current = self.root
        for ch in prefix:
            if not current.has_child(ch):
                return None  # Prefix not found
            current = current.get_child(ch)
        return current

    def collect_words(self, node, prefix, list_of_words):
        if node.is_end_of_word:
            list_of_words.append(prefix)

        for i in range(self.Node.ALPHABET_SIZE):
            if node.children[i]:
                self.collect_words(node.children[i], prefix + chr(i + ord("a")), list_of_words)


# Driver code
trie = Trie()

trie.insert("how")
trie.insert("house")
trie.insert("hi")
trie.insert("app")
trie.insert("apple")

print(trie.find("hi"))  # True
print(trie.find("how"))  # True
print(trie.find("home"))  # False
print(trie.find("appl"))  # False

trie.insert("appl")
print(trie.find("appl"))  # Now it's true

trie.remove("appl")
print(trie.find("appl"))
print(trie.find("app"))
print(trie.find("apple"))

trie.insert("are")
trie.insert("apply")
print(trie.words_with_prefix("a"))
print(trie.words_with_prefix("app"))
