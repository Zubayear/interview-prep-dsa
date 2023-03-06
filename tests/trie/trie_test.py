import pytest

from trie.Trie import Trie


@pytest.fixture()
def trie_data():
    trie = Trie()
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("pear")
    trie.insert("peach")

    return trie


def test_search(trie_data):
    t = trie_data
    assert t.search("banana") == True
    assert t.search("king") == False


def test_get_word(trie_data):
    t = trie_data
    assert t.get_word("a") == ['apple']
    assert t.get_word("p") == ['pear', 'peach']
