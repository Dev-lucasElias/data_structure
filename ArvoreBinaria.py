from element.Node import Node
import random
class tree:
      def __init__(self,node ) -> None:
            if all(isinstance(n, Node) for n in node):
                  self.__root = node[0]
                  for i in node:
                        if i != node[0]:
                              self.inNode(i)
            if isinstance(node,Node):
                  self.__root = node
            
            self.__arrayInorder=[]
            self.__arrayPreorder=[]
            self.__arrayPosorder=[]
            
      
      def inNode (self, node):
            if isinstance( node,list):
                  for i in node:
                        self.verifyRootIN(self.__root,i)
            if isinstance(node,Node):
                  self.verifyRootIN(self.__root,node)
            
      def verifyRootIN (self, root, node):
            if root.getValue() > node.getValue():
                  if root.getLeft() == None:
                        root.setLeft(node)
                  else:
                        self.verifyRootIN(root.getLeft(),node)
            else:
                  if root.getRight() == None:
                        root.setRight(node)
                  else:
                        self.verifyRootIN(root.getRight(),node)
      
      def verifyRootLeft(self, root):
            if root.getLeft() != None:
                  self.verifyRootLeft(root.getLeft())
            self.__arrayInorder.append(root.getValue())
            if root.getRight() != None:
                  self.verifyRootLeft(root.getRight())
                  
      def verifyRootFirst(self, root):
            self.__arrayPreorder.append(root.getValue())
            if root.getLeft() != None:
                  self.verifyRootFirst(root.getLeft())
            if root.getRight() != None:
                  self.verifyRootFirst(root.getRight())
      
      def verifyRootLast(self, root):
            if root.getLeft() != None:
                  self.verifyRootLast(root.getLeft())
            if root.getRight() != None:
                  self.verifyRootLast(root.getRight())         
            self.__arrayPosorder.append(root.getValue())
                                      
      def Inorder(self):
            raiz = self.__root
            self.verifyRootLeft(raiz)
            print(self.__arrayInorder)
            self.__arrayInorder = [None]
            
      def Preorder(self):
            raiz = self.__root
            self.verifyRootFirst(raiz)
            print(self.__arrayPreorder)
            self.__arrayPreorder = [None]
      
      def Posorder(self):
            raiz = self.__root
            self.verifyRootLast(raiz)
            print(self.__arrayPosorder)
            self.__arrayPosorder = [None]
            
                        

#teste
array = []
for _ in range(20):
    array.append(Node(random.randint(0, 1000)))

minhaArvore = tree(array)
minhaArvore.Inorder()
minhaArvore.Preorder()
minhaArvore.Posorder()