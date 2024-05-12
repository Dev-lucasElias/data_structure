from element.element import Element

class hash:
            def __init__(self,nElements,fc) -> None:
                  self.__fc = fc
                  self.__nElements = nElements
                  self.__tabelaEspalhamento = [None] * int(nElements/fc)
            
            def hash(self,value):
                  return int(value % int(self.__nElements/self.__fc))
            
            def inElement(self,element):
                  hash = self.hash()
                  self.__tabelaEspalhamento[hash].append(element)
                  