"""
GeeksForGeeks

Given a sorted dictionary of an alien language, find order of characters

https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()

class Node:
    def __init__(self, letter):
        self.parents = set()
        self.children = set()
        self.letter = letter
    
    def __repr__(self):
        return f"<{self.letter}>"

letter2node = {letter: Node(letter) for letter in alphabet}

def add_child(parent, child):
    parent.children.add(child)
    child.parents.add(parent)
    for gp in parent.parents:
        add_child(gp, child)
    for gc in child.children:
        add_child(parent, gc)


def find_alien_alphabet(sorted_words):

    for word_ix in range(len(sorted_words)-1):
        i = 0
        word1 = sorted_words[word_ix]
        word2 = sorted_words[word_ix+1]

        i_limit = min(len(word1), len(word2))

        while i < i_limit and word1[i] == word2[i]:
            i += 1

        if i < i_limit:              
            add_child(letter2node[word1[i]], letter2node[word2[i]])
    
    return sort_by_children()


def sort_by_children():
    sorted_arr = []
    nodes = [node for node in letter2node.values() if (len(node.children) != 0 or len(node.parents) != 0)] 
    while nodes:
        max_children = -1
        biggest_node = None
        for node in nodes:

            if len(node.children) > max_children:
                max_children = len(node.children)
                biggest_node = node
        print(biggest_node)
        nodes.remove(biggest_node)
        sorted_arr.append(biggest_node.letter)

    return sorted_arr
        


words = ["baa", "abcd", "abca", "cab", "cad"]
print(find_alien_alphabet(words))