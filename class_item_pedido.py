class ItemPedido:
    def __init__(self, produto, quantidade):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__preco_item = produto._preco * quantidade

    def calcular_preco(self):
        total = 0
        for item in self.__itens_pedidos:
            total += item._preco_item
        return total

    @property
    def _produto(self):
        return self.__produto

    @_produto.setter
    def _produto(self, value):
        self.__produto = value

    @property
    def _quantidade(self):
        return self.__quantidade

    @_quantidade.setter
    def _quantidade(self, value):
        self.__quantidade = value

    @property
    def _preco_item(self):
        return self.__preco_item
