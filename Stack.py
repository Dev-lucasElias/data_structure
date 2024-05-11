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

class stack:
      def __init__(self):
            self.__last = None
            self.__count = 0

      def getLen(self):
          return self.__count

      def pop (self,novo: Element):
            if self.__count == 0:
                  self.__last = novo
                  self.__count += 1
            else:
                  novo.setNext(self.__last)
                  self.__last = novo
                  self.__count += 1

      def push (self):
           new_last = self.__last.getNext()
           if self.__count == 0:
                return False
           else:  
                self.__last = new_last

      def PrintStack(self):
           element_moment = self.__last
           for i in self.__count:
                print(element_moment.getValue())
                print(" ")
                element_moment = element_moment.getNext()

e1 = Element("lucas")
e2 = Element("evandro")
e3 = Element("Daniel")

pilha = stack()
pilha.pop(e1)
pilha.pop(e2)
pilha.pop(e3)
pilha.PrintStack()
            
              

 