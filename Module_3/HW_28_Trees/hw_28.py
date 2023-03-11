# Розширити структуру, яку побудували на уроці,
# можливістю вставки дерева в наявне дерево та видалення піддерева з дерева, що існує.

class TreeNode:

    def __init__(self, root_name):
        self.root_name = root_name
        self.children = []

    def __str__(self):
        return self.root_name

    def __repr__(self):
        return self.root_name

    def __eq__(self, other):
        return self.root_name == other.root_name

    def add_child(self, child_name):
        new_child = TreeNode(child_name)
        if new_child.root_name == self.root_name:
            return False
        if new_child not in self.children:
            self.children.append(new_child)
            return True
        else:
            return False

    def show_children(self, node_name):
        if node_name in self.children:
            return


t = TreeNode('a')
t.add_child('b')
t.add_child('b')
t.add_child('c')
print(t.children)
