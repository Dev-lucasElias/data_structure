from element.element import Element

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


 