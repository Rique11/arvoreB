

class Node: 
    def __init__(self, folha = True): 
        self.chaves = []
        self.filhos = []
        self.folhas = folha
    
class BTree: 
    def __init__(self, valor):
        self.raiz = Node()
        self.valor = valor

    def insere(self, chave): 
        raiz = self.raiz
        if len(raiz.chaves) == (2*self.valor) - 1: 
            raizNova = Node(False)
            raizNova.filhos.append(self.raiz)
            self.split(raizNova, 0)
            self.raiz = raizNova
        self.insereNaoCheia(self.raiz, chave)
    
    def insereNaoCheia(self, x, chave):
        i = len(x.chaves) - 1
        if x.folhas: 
            x.chaves.append(None)
            while i >= 0 and chave < x.chaves[i-1]:
                x.chaves[i] = x.chaves[i-1]
                i-=1
            x.chaves[i] = chave
        else: 
            while i >= 0 and chave < x.chaves[i]:
                i-=1
            i+=1
            if len(x.filhos[i].chaves) == (2*self.valor) - 1: 
                self.split(x,i)
                if chave > x.chaves[i]: 
                    i+=1
                self.insereNaoCheia(x.filhos[i], chave)

    def split(self, raizNova, aux): 
        valor = self.valor
        y = raizNova.filhos[aux]
        z = Node(y.folhas)
        raizNova.filhos.insert(aux+1, z)
        raizNova.chaves.insert(aux, y.chaves[valor - 1])
        z.chaves = y.chaves[valor:(2 * valor) - 1]
        y.chaves = y.chaves[0:valor - 1]

    def buscaElem(self, x, chave): 
        i = 0
        while i < len(x.chaves) and (x.chaves[i] is not None) and chave > x.chaves[i]:
            i+=1
        if i < len(x.chaves) and chave == x.chaves[i]:
            return True
        elif x.folhas: 
            return False
        else: 
            return self.buscaElem(x.filhos[i], chave)    


#Aplicacao 

arvoreB = BTree(2)
chaves = [2, 7, 5, 8, 9, 12, 6, 3]
for chave in chaves: 
    arvoreB.insere(chave)

resultado = arvoreB.buscaElem(arvoreB.raiz, 8)
print(f"A chave esta presente? {resultado} ")

