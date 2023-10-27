from class_item_pedido import ItemPedido

class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codido_pedido):
        self.__codigo_pedido = codido_pedido
        self.__status = 0  # 0 = aberto, 1 = finalizado/pago
        # criando uma estrutura map em python para armzenar itens do pedido
        self.__itens_pedidos = []
        self.__cliente = None  # Adicionando um atributo para o cliente
        self.__funcionario = None  # Adicionando um atributo para o funcionário

    def adicionar_produto(self, produto, quantidade):
        item_pedido = ItemPedido(produto, quantidade)
        self.__itens_pedidos.append(item_pedido)

    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _codigo_pedido(self):
        return self.__codigo_pedido

    @_codigo_pedido.setter
    def _codigo_pedido(self, value):
        self.__codigo_pedido = value

    @property
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def funcionario(self):
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario

    def adicionar_item_ao_pedido(self, itempedido):
        self.__itens_pedidos.append(itempedido)

    def remover_item_pedido(self, codigo_item):
        if 0 <= codigo_item < len(self._itens_pedidos):
            self._itens_pedidos.pop(codigo_item)
        else:
            print("Item não encontrado.")

    def concluir_pedido(self):
        self._status = 1

    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))
        # return self.__itens_pedidos.__sizeof__

    def calcular_preco_total(self):
        total = 0
        for item in self.__itens_pedidos:
            total += item._preco_item
        return total

    def __str__(self):
        str_line = "** INÍCIO DAS INFORMAÇÕES DO PEDIDO **"
        str_line += f"\nCÓDIGO DO PEDIDO: {self._codigo_pedido}"
        str_line += f"\nSTATUS DO PEDIDO: {'Finalizado/Pago' if self._status == 1 else 'Aberto'}"
        str_line += f"\nQUANTIDADE DE ITENS DO PEDIDO: {self.quantidade_itens_pedido()}"
        dbl_preco_total = 0.0
        for i, item in enumerate(self._itens_pedidos):
            str_line += f"\n\t #ITEM: {i}"
            str_line += f"\n\tPRODUTO: {item._produto._descricao}"
            str_line += f"\n\tQTD (#): {item._quantidade}"
            str_line += f"\n\tSUBTOTAL (R$): {item._preco_item}"
            dbl_preco_total += item._preco_item
        str_line += f"\nPREÇO TOTAL DO PEDIDO: {dbl_preco_total}"

        # Adicionar informações do cliente e do funcionário
        if self.__cliente is not None:
            str_line += f"\nCLIENTE: {self.__cliente._nome}"  # Use o atributo correto do cliente
        if self.__funcionario is not None:
            str_line += f"\nFUNCIONÁRIO: {self.__funcionario._nome}"  # Use o atributo correto do funcionário

        str_line += "\n** FIM DAS INFORMAÇÕES DO PEDIDO **"
        return str_line