from class_pessoas import Pessoas

class Cliente(Pessoas):
    def __init__(self, nome, cpf, email, data_nascimento, telefone, endereco_entrega, senha):
        super().__init__(nome, cpf, email, data_nascimento, telefone, endereco_entrega)
        self.__senha = senha

    @property
    def _senha(self):
        return self.__senha

    @_senha.setter
    def _senha(self, value):
        self.__senha = value

    def listar(self):
        print(f"Cliente: {self._nome}, CPF: {self._cpf}, Email: {self._email}, Data de nascimento: {self._data_nascimento}")
