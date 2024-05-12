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

class queue:
      def __init__(self):
            self.__last = None
            self.__count = 0
            self.__first = None

      def getLen(self):
          return self.__count

      def queueIn (self,novo: Element):
            if self.__count == 0:
                  self.__last = novo
                  self.__count += 1
                  self.__first = novo
            else:
                  novo.setNext(self.__first)
                  self.__first = novo
                  self.__count += 1

      def queueOut (self):
            if self.__count == 0:
                  return False
            elif self.__count == 1:
                  self.__first = None
                  self.__last = None
            else:
                  cursor = self.__first
                  for i in range(self.__count):
                        if i != 1:
                              cursor = cursor.getNext()
                        if i == self.__count-1:
                              self.__last = cursor
            self.__count -=1                        
            
      def PrintQueue(self):
           element_moment = self.__first
           for i in range(self.__count):
                print(element_moment.getValue())
                element_moment = element_moment.getNext()

# ================ TEST ===============================            
              
e1 = Element("lucas")
e2 = Element("evandro")
e3 = Element("Daniel")

fila = queue()
fila.queueIn(e1)
fila.queueIn(e2)
fila.queueIn(e3)
fila.queueOut()
fila.queueOut()
fila.queueIn(e2)
fila.queueIn(e1)
print(fila.getLen())
fila.PrintQueue()

 