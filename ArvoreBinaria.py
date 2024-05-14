from element.Node import Node

class tree:
      def __init__(self,node ) -> None:
            if isinstance(node,list(Node)):
                  pass
            if isinstance(node,Node):
                  self.__root = node
            
      
      def inNode (self, node):
            if isinstance(node,list(Node)):
                  for i in node:
                        self.verifyRootIN(self.__root,i)
            if isinstance(node,Node):
                  self.verifyRootIN(self.__root,node)
            
      def verifyRootIN (self, root: Node, node):
            if root.getValeu > Node:
                  if root.getLeft() == None:
                        root.setLeft(node)
                  else:
                        self.verifyRootIN(root.getLeft,node)
            else:
                  if root.getRight() == None:
                        root.setRight(node)
                  else:
                        self.verifyRootIN(root.getRight,node)