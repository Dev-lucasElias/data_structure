from element.element import Element
from ListaDencadeada import ListaEncadeada
class hash:
            def __init__(self,nElements,fc) -> None:
                  self.__fc = fc
                  self.__nElements = nElements
                  self.__tabelaEspalhamento = [ListaEncadeada() for _ in range(int(nElements / fc))]
            
            def hash(self,value):
                  return int(value % int(self.__nElements/self.__fc))
            
            def inElement(self,element: Element):
                  hash = self.hash(element.getValue())
                  self.__tabelaEspalhamento[hash].inserirComoPrimeiro(element)
                  
            def OutElement(self,element):
                  hash = self.hash(element.getValue())
                  self.__tabelaEspalhamento[hash].ExcluirElemento(element)
                  