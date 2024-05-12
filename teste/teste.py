from element.element import Element
from fila import queue
from Stack import stack


# ================ TEST FILA ===============================            
              
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


# ================ TEST PILHA ===============================            
              
e1 = Element("lucas")
e2 = Element("evandro")
e3 = Element("Daniel")

pilha = stack()
pilha.pop(e1)
pilha.pop(e2)
pilha.pop(e3)
pilha.push()
pilha.push()
pilha.pop(e2)
print(pilha.getLen())
pilha.PrintStack()
