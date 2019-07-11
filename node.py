class node(object):
    def __init__(self, elemento, valor, start=False, final=False):
        self.elemento = elemento
        self.valor = valor
        

    def set_proximo(self, node):
        self.proximo = node
    def get_proximo(self):
        return self.proximo

if __name__ == "__main__":
    novo = node(0,'T')
    outro = node(1,'A')
    novo.set_proximo(outro)
    print(novo.get_proximo().valor)





