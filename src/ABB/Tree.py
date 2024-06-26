from ABB.Node import Node

class Tree:
    def __init__(self, data):
        self.root = Node(data)
        
    def __add_nodes(self, node, data, position):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                node.left.position = position
            else:
                self.__add_nodes(node.left, data, position)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                node.right.position = position
            else:
                self.__add_nodes(node.right, data, position)
    
    def __inorder(self, node):
        if node is not None:
            self.__inorder(node.left)
            print(node.data, end=", ")
            self.__inorder(node.right)
    
    def __preorder(self, node):
        if node is not None:
            print(node.data, end=", ")
            self.__preorder(node.left)
            self.__preorder(node.right)
    
    def __postorder(self, node):
        if node is not None:
            self.__inorder(node.left)
            self.__inorder(node.right)
            print(node.data, end=", ")
            
    def __search(self, node, search):
        if node is None:
            return None
        if node.data == search:
            return node
        if search < node.data:
            return self.__search(node.left, search)
        else:
            return self.__search(node.right, search)
            
    def add_node(self, data, position):
        self.__add_nodes(self.root, data, position)
        
    def inorder_route(self):
        print("\nArbol Inorder")
        self.__inorder(self.root)
        print("")
    
    def preorder_route(self):
        print("\nArbol preorder")
        self.__preorder(self.root)
        print("")
    
    def postorder_route(self):
        print("\nArbol postorder")
        self.__postorder(self.root)
        print("")
        
    def search(self, search):
        return self.__search(self.root, search)