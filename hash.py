from element.element import Element
from ListaDencadeada import ListaEncadeada
import random

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
                  
            def ViewHash(self):
                  n = 0
                  for i in self.__tabelaEspalhamento:
                        print(f"posicao {n}", end = " ") 
                        i.PrintList()
                        n +=1
                        
            def BuscaByValue(self,value):
                  hash = self.hash(value)
                  self.__tabelaEspalhamento[hash].ExcluirElemento(self.__tabelaEspalhamento[hash].buscarElemento(value))
                        
            def getNelement(self):
                  return self.__nElements
 
     
      
      
      
      
      
      
      
    