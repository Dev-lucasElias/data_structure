from element.element import Element

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
                self.__count -= 1

      def PrintStack(self):
           element_moment = self.__last
           for i in range(self.__count):
                print(element_moment.getValue())
                print(" ")
                element_moment = element_moment.getNext()


 