import config

comparisons = 0
class bstree:
    def __init__(self):
        self.verbose = config.verbose
        self.insertions = 0

    def height(self):
        if (self.tree()):
            return 1 + max(self.left.height(), self.right.height())  # sum all left nodes, and right nodes, and return the larger + 1 as root node is considered to be height 1
        return 0 # no tree hence height = 0

    def tree(self):
        return hasattr(self, 'value')

    def insert(self, value):
        if self.tree():
            if value == self.value:
                self.insertions -= 1
                return # do nothing as this value already exists in the BST so it's a duplicate

            self.insertions += 1

            if value < self.value:
                self.left.insert(value)  # insert word as left child of current node
            else:
                self.right.insert(value)  # insert word as right child of current node

        else: # the value is either root node or must be a child to an external node
            self.insertions += 1
            self.value = value
            self.left = bstree()  # create left child as object of class
            self.right = bstree()  # create right child as object of class

    def find(self, value):
        global comparisons
        if self.tree():
            if self.value == value:
                comparisons += 1
                return True # this word is correctly spelled as it exists in BST
            elif value < self.value:
                comparisons += 1
                return self.left.find(value)  # recursively call with value as left child
            elif value > self.value:
                comparisons += 1
                return self.right.find(value)  # recursively call with value sa right child
        comparisons += 1
        return False  # word not in BST, hence incorrectly spelled

    def print_set_recursive(self, depth):
        if (self.tree()):
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.value)
            self.left.print_set_recursive(depth + 1)
            self.right.print_set_recursive(depth + 1)

    def print_set(self):
        print("Tree:\n")
        self.print_set_recursive(0)

    def print_stats(self):
        print("Height of tree:",self.height(),
              "\nNumber of insertions:", self.insertions,
              "\nNumber of comparisons:", comparisons,
              "\nAverage comparisons per insertions:", comparisons/self.insertions)