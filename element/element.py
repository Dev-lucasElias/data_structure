class Element:
      def __init__(self, value) -> None:
            self.__value = value
            self.__next = None

      def setNext(self,next):
            self.__next = next
      
      def getNext(self):
            return self.__next

      def getValue(self):
            return self.__value
    
      def getAnterior(self):
            return self.__anterior
      
      def setAnterior(self, anterior):
            self.__anterior = anterior