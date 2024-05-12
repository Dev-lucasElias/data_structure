from element.element import Element

class ListaEncadeada:
    def __init__(self) -> None:
        self.__primeiro = None
        self.__ultimo = None
        self.__cursor = None
        self.__tamanhoDaLista = 0

    def __avancarKPosicoes(self, K: int): # se caso ultrapassar a lista, considera-se o ultimo
        for i in range(K):
            self.__cursor = self.__cursor.getNext() if self.__cursor.getNext() != None else self.__cursor
    
    def __retrocederKPosicoes(self, K: int): # se caso ultrapassar a lista, considera-se o primeiro
        for i in range(K):
            self.__cursor = self.__cursor.elementoAnterior() if self.__cursor.getAnterior() != None else self.__cursor
    
    def __irParaOPrimeiro(self): #cursor se move para o primeiro
        self.__cursor = self.__primeiro
    
    def __irParaOUltimo(self): #cursor se move para o ultimo
        self.__cursor = self.__ultimo
    
    def getPrimeiro(self): #retorna o primeiro
        return self.__primeiro
    
    def getUltimo(self): #retorna o ultimo
        return self.__ultimo
    
    def irParaPosicaok(self,k): #move o cursor para a posição k
        self.__irParaOPrimeiro()
        self.__avancarKPosicoes(k)
    
    def inserirComoPrimeiro(self, novo_primeiro: Element): #não move o cursor
        self.__irParaOPrimeiro()

        if  self.__tamanhoDaLista == 0:
            self.__ultimo = novo_primeiro
        else:
            novo_primeiro.setNext(self.__primeiro)
            self.__primeiro.setAnterior(novo_primeiro)

        self.__primeiro = novo_primeiro
        self.__tamanhoDaLista += 1
    
    def inserirComoUltimo(self, novo_ultimo: Element): #não move o cursor
        self.__irParaOUltimo()

        if  self.__tamanhoDaLista == 0:
            self.__primeiro = novo_ultimo
        else:
            self.__ultimo.setNext(novo_ultimo)
            novo_ultimo.setAnterior(self.__ultimo)

        self.__ultimo = novo_ultimo
        self.__tamanhoDaLista += 1

    def inserirAntesDoAtual (self, novo: Element): #cursor não se movimenta
        if self.__cursor == self.__primeiro:
            self.inserirComoPrimeiro(novo)
        else:
            anterior = self.__cursor.getAnterior()
            self.__cursor.setAnterior(novo)
            novo.setNext(self.__cursor)
            anterior.setNext(novo)
            novo.setAnterior(anterior)
            self.__tamanhoDaLista += 1
    
    def inserirAposAtual(self, novo: Element): #cursor não se movimenta
        if self.__cursor == self.__ultimo:
            self.inserirComoUltimo(novo)
        else:
            proximo = self.__cursor.getNext()
            self.__cursor.setNext(novo)
            novo.setAnterior(self.__cursor)
            proximo.setAnterior(novo)
            novo.setNext(proximo)
            self.__tamanhoDaLista += 1
    
    def inserirNaPosicao(self, novo: Element, k: int): #não move o cursor
        if k == 0:
            self.inserirComoPrimeiro(novo)
        elif k >= self.__tamanhoDaLista:
            self.inserirComoUltimo(novo)
        else:
            copiaCursor = self.__cursor
            self.__irParaOPrimeiro()
            self.__avancarKPosicoes(k)
            if self.__tamanhoDaLista > 0:
                anterior = self.__cursor.getAnterior()
                proximo = self.__cursor
                novo.setNext(proximo)
                novo.setAnterior(anterior)
                if anterior == None:
                    self.__primeiro = novo
                else:
                    anterior.setNext(novo)
                proximo.setAnterior(novo)
                self.__cursor = copiaCursor
                self.__tamanhoDaLista += 1
            else:
                self.inserirComoPrimeiro(novo)
            
    def ExcluirAtual(self): #move o cursor para o proximo dele antes de ser exluido, mantendo na mesma posição, caso não tenha proximo, move para o anterior
        if self.__cursor != None:
            anteriorDoCursor = self.__cursor.getAnterior()
            proximoDoCursor = self.__cursor.getNext()
            if anteriorDoCursor != None:
                anteriorDoCursor.setNext(proximoDoCursor)
            if proximoDoCursor != None:
                proximoDoCursor.setAnterior(anteriorDoCursor)
                self.__cursor = proximoDoCursor
                if anteriorDoCursor == None:
                    self.__primeiro = self.__cursor
            else:
                if anteriorDoCursor == None:
                    self.__cursor = None
                    self.__ultimo = None
                    self.__primeiro = None
                else:
                    self.__cursor = anteriorDoCursor
                    self.__ultimo = self.__cursor
            self.__tamanhoDaLista -= 1
        
    def ExcluirUltimo(self): #Move o cursor se ele estiver no ultimo elemento
        copiaCursor = self.__cursor
        self.__irParaOUltimo()

        if self.__ultimo != None:
            anteriorDoUltimo = self.__ultimo.getAnterior()
            if anteriorDoUltimo != None:
                if self.__cursor == self.__ultimo:
                    self.__cursor == anteriorDoUltimo
                anteriorDoUltimo.setNext(None)
                self.__ultimo = anteriorDoUltimo
                self.__cursor = copiaCursor
            else:
                self.__ultimo = None
                self.__primeiro = None
                self.__cursor = None
            self.__tamanhoDaLista -= 1
    
    def ExcluirPrimeiro(self): #Move o cursor se ele estiver no primeiro elemento
        copiaCursor = self.__cursor
        self.__irParaOPrimeiro()

        if self.__primeiro != None:
            proximoDoPrimeiro = self.__primeiro.getNext()
            if proximoDoPrimeiro != None:
                if self.__cursor == self.__primeiro:
                    self.__cursor == proximoDoPrimeiro
                proximoDoPrimeiro.setAnterior(None)
                self.__primeiro = proximoDoPrimeiro
                self.__cursor = copiaCursor
            else:
                self.__ultimo = None
                self.__primeiro = None
                self.__cursor = None
            self.__tamanhoDaLista -= 1
    
    def ExcluirElemento(self, valor: int): #Move o cursor caso ele seja o elemento excluido
        copiaCursor = self.__cursor
        if self.buscarElemento(valor) == True:
            self.ExcluirAtual()
            if copiaCursor.getValue() != valor:
                self.__cursor = copiaCursor
        
    def ExcluirDaPosicao(self, k: int): #Move o cursor caso ele seja o elemento excluido
        if k == 0:
            self.ExcluirPrimeiro()
        elif k >= self.__tamanhoDaLista:
            self.ExcluirUltimo()
        else:
            copiaCursor = self.__cursor
            self.__irParaOPrimeiro()
            self.__avancarKPosicoes(k)
            if self.__tamanhoDaLista > 0:
                anterior = self.__cursor.getAnterior()
                proximo = self.__cursor.getNext()
                if anterior == None:
                    self.__primeiro = proximo
                else:
                    anterior.setNext(proximo)
                if proximo == None:
                    self.__ultimo = anterior
                else:
                    proximo.setAnterior(anterior)
                if copiaCursor == self.__cursor:
                    self.__cursor = proximo
                else:
                    self.__cursor = copiaCursor
                self.__tamanhoDaLista -= 1

    def buscarElemento(self, valor: int): #cursor se move para o elemento buscado caso seja encontrado
        fake = Element(valor)
        copiaCursor = self.__cursor
        self.inserirComoUltimo(fake)

        self.__irParaOPrimeiro()
        while True:
            if self.__cursor.getValue() == valor:
                if self.acessarAtual() == fake:
                    self.ExcluirUltimo()
                    self.__cursor = copiaCursor
                    return False
                self.ExcluirUltimo()
                return True
            self.__avancarKPosicoes(1)

    def acessarAtual(self): #nao move o cursor
        return self.__cursor

    def getTamanhoLista(self): #nao move o cursor
        return self.__tamanhoDaLista
    
    def avancaCursor(self): #avanca o cursor em 1 posicao
        self.__avancarKPosicoes(1)

    def retrocedeCursor(self): #retrocede o cursor em 1 posicao
        self.__retrocederKPosicoes(1)

    def recuarCursorParaoPrimeiro(self): #move o cursor para o primeiro elemento
        self.__irParaOPrimeiro()
    
    def PrintList(self):
        visualizacaoLista = []
        self.__irParaOPrimeiro()
        for i in range (self.getTamanhoLista()):
            visualizacaoLista.append(self.acessarAtual().getValue())
            self.avancaCursor()
        print(visualizacaoLista)
        self.__irParaOPrimeiro()

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)
e7 = Element(7)
