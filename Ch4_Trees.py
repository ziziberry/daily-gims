class TreeNode(object): 
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data=val

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_right(self):
        return self.parent and self.parent.right == self

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_root(self):
        return (not self.parent)

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def replaceNodeData(self,data,lc,rc):
        self.data = data
        self.left = lc
        self.right = rc
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self

    def print_node(self):
        print self.data

class Tree(object):
    def __init__(self, root=None):
        self.root=root
        if root is not None: 
            self.size = 1
        else: 
            self.size = 0

    def size(self):
        return self.size

    def helper_insert(self, val, current_node):
        if val < current_node.get_data():
            if current_node.has_left_child():
                self.helper_insert(val, current_node.left)
            else: 
                current_node.left=TreeNode(val, parent=current_node)
        else:
            if current_node.has_right_child():
                self.helper_insert(val, current_node.right)
            else: 
                current_node.right=TreeNode(val, parent=current_node)

    def insert(self, val):
        if self.root: 
            self.helper_insert(val, self.root)
        else: 
            self.root=TreeNode(val)
        self.size+=1

    def find(self, val):
        if self.root:
            # print "Hello from Find()"
            # self.root.print_node()
            val_node=self.helper_find(val, self.root)
            # print "Hello from after val_node"
            if val_node: 
                print val_node.get_data()
                return val_node
            else: 
                print "Value Not Found"
                return
        else: 
            return "Empty Tree"

    def helper_find(self, val, current_node):
        if val < current_node.get_data():
            if current_node.left:
                return self.helper_find(val, current_node.left)
            else: 
                return None
        elif val > current_node.get_data():
            if current_node.right:
                return self.helper_find(val, current_node.right)
            else: 
                return None
        elif val == current_node.get_data():
            return current_node
        else:
            return None

    # overwrites the "in" operator
    def __contains__(self, val):
        if self.helper_find(val,self.root):
            return True
        else:
            return False

    def inOrderTraversal(self, node):
        if node: 
            self.inOrderTraversal(node.left)
            node.print_node()
            self.inOrderTraversal(node.right)

    def preOrderTraversal(self, node):
        if node: 
            node.print_node()
            self.inOrderTraversal(node.left)
            self.inOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node:
            self.inOrderTraversal(node.left)
            self.inOrderTraversal(node.right)
            node.print_node()

    def findMin(self, node):
        current = node
        while current.has_left_child():
            current = current.left
        return current

    def delete(self, val):
        if self.size == 1 and val == self.root.get_data():
            self.size-=1
            self.root=None
        elif self.size == 1 and val != self.root.get_data():
            print "Value not Found"
            return
        elif self.size > 1: 
            val_node = self.helper_find(val, self.root)     
            if val_node: 
                self.deleteNode(val_node)
                self.size-=1
            else: 
                print "Value Not Found"
                return

    # overwrites the "del" operator
    def __delitem__(self, val):
        self.delete(val)

    def deleteNode(self, node):
        if node.is_leaf():
            if node.is_left():
                node.parent.left = None
            else:
                node.parent.right = None
            node.parent = None
        elif node.has_both_children():
            successor = self.findMin(node.right)
            if successor has a right leaf: 

            else: 
            # find minimum value in the right side of the branch
            print "Work in progress"

        else:
            if node.is_left():
                if node.has_left_child():
                    node.parent.left = node.left
                    node.left.parent = node.parent
                    node.parent = None
                elif node.has_right_child():
                    node.parent.left = node.right
                    node.right.parent = node.parent
                    node.parent = None
            elif node.is_right():
                if node.has_left_child():
                    node.parent.right = node.left
                    node.left.parent = node.parent
                    node.parent = None
                elif node.has_right_child():
                    node.parent.right = node.right
                    node.right.parent = node.parent
                    node.parent = None
            else: # node is root node, has no parent node
                if node.has_left_child():
                    node.left.parent = None
                    self.root = node
                elif node.has_right_child():
                    node.right.parent = None
                    self.root = node





root = TreeNode(5)
tree1 = Tree(root)

tree1.insert(2)
tree1.insert(9)
tree1.insert(0)
tree1.insert(1)
tree1.insert(6)
tree1.insert(11)
tree1.insert(10)

# print tree1.size
# tree1.inOrderTraversal(tree1.root)

# print "Deleting 9"

# tree1.delete(9)

# tree1.inOrderTraversal(tree1.root)

tree1.findMin(tree1.root.right).print_node()

# for i in xrange(10):
#     tree1.insert(i)
# tree1.find(4).print_node()
# tree1.find(4)
# tree1.inOrderTraversal(tree1.root)
# tree1.root.print_node()
# tree1.root.left.print_node()

# print 7 in tree1





