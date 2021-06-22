import random

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Tree:
    def __init__(self, tree_list):
        self.tree_list = tree_list
        self.root = Node(random.choice(self.tree_list))

    def add_val(self, val, current_node):
        if val < current_node.val and current_node.left == None:
            current_node.left = Node(val)

        elif val >= current_node.val and current_node.right == None:
            current_node.right = Node(val)

        elif val >= current_node.val and current_node.right != None:
            self.add_val(val, current_node.right)

        elif val < current_node.val and current_node.left != None:
            self.add_val(val, current_node.left)

    def search(self, val, current):
        if current.val == val:
            return True

        if current.val > val:
            if not current.left:
                return False
            return self.search(val, current.left)

        elif current.val < val:
            if not current.right:
                return False
            return self.search(val, current.right)

    def init_tree(self):
        for node in self.tree_list:
            if node != self.root:
                self.add_val(node, self.root)


tree_list = random.sample(range(0, 30), 10)
tree = Tree(tree_list)
tree.init_tree()
print(tree.search(22, tree.root))



