from element.element import Element
from Fila import queue
from Stack import stack
from ListaDencadeada import ListaEncadeada

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


# ================ TEST LISTA DUPLAMENTE ENCADEADA ===============================            

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)
e7 = Element(7)

# --------Montando a lista------------
lista = ListaEncadeada()
lista.inserirComoUltimo(e6)
lista.inserirComoPrimeiro(e5)
lista.inserirComoPrimeiro(e4)
lista.inserirComoPrimeiro(e3)
lista.inserirComoPrimeiro(e2)
lista.inserirComoPrimeiro(e1)
print(" --------IMPRIMINDO LISTA INICIAL------------")
lista.PrintList()#IMPRIME

if lista.buscarElemento(4):
    lista.ExcluirAtual()
print(" --------EXCLUINDO O NUMERO 4------------")
lista.PrintList()#IMPRIME

lista.inserirComoPrimeiro(e4)
print("--------INserindo o e4 na primeira posição------------")
lista.PrintList()#IMPRIME

lista.inserirNaPosicao(e7, 5)
print(" --------inserindo um novo elemento no lugar ordenado------------")
lista.PrintList()#IMPRIME

lista.ExcluirUltimo()
lista.ExcluirPrimeiro()
print("--------Excluindo primeiro e ultimo------------")
lista.PrintList()#IMPRIME

lista.ExcluirElemento(3)
print(" --------Excluir um elemento específico------------")
lista.PrintList()#IMPRIME

lista.ExcluirDaPosicao(1)
print(" --------Excluir um elemento pela posição------------")
lista.PrintList()#IMPRIME

lista.irParaPosicaok(1)
print(" --------Ir para posicao 1 e inserir antes e depois------------")
print("Cursor",lista.acessarAtual().getValor())
lista.inserirAntesDoAtual(e6)
lista.inserirAposAtual(e3)
lista.PrintList()#IMPRIME


# ================ TEST HASH ===============================    