class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.parent = None 
        self.left = None
        self.right = None

    def add_left(self, data=None):
        left_node = Node(data=data)
        left_node.parent = self
        self.left = left_node
        return left_node

    def add_right(self, data=None):
        right_node = Node(data=data)
        right_node.parent = self
        self.right = right_node
        return right_node

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()

        traversal += [self.data]

        if self.right:
            traversal += self.right.inorder()

        return traversal

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()

        if self.right:
            traversal += self.right.postorder()

        traversal += [self.data]

        return traversal

    def preorder(self):
        traversal = []
        traversal += [self.data]

        if self.left:
            traversal += self.left.preorder()

        if self.right:
            traversal += self.right.preorder()

        return traversal

    def sexp(self):
        sexp = [self.data] 

        if self.left:
            sexp.append(self.left.sexp()) 
        else:
            sexp.append(None)

        if self.right:
            sexp.append(self.right.sexp()) 
        else:
            sexp.append(None)

        return sexp

    def insert(self, data):
        if data < self.data:
            try:
                self.left.insert(data)
            except AttributeError:
                self.add_left(data)
        elif data > self.data:
            try:
                self.right.insert(data)
            except AttributeError:
                self.add_right(data)
        elif data == self.data:
            self.left.insert(data)
        else:
            self.data = data

    @classmethod
    def mktree(cls, iterable):
        head, tail = iterable[0], iterable[1:]
        root = Node(data=head)
        for item in tail:
            root.insert(item)
        return root


    @property
    def sibling(self):
        parent = self.parent
        left, right = parent.left, parent.right
        return right if left is self else left 

    def __repr__(self):
        return "Node(data={})".format(self.data)


    def __str__(self):
        return str(self.inorder())
