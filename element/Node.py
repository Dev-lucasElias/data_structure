
class Node:
      def __init__(self, value) -> None:
            self.__value = value
            self.__left = None
            self.__right = None
      
      def getLeft(self):
            return self.__left
      def getRight(self):
            return self.__right
      
      def setLeft(self,novo):
            self.__left = novo
            
      def setRight(self,novo):
            self.__right = novo
      
      def getValeu(self):
            return self.__value