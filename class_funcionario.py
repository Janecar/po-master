from class_pessoas import Pessoas

class Funcionario(Pessoas):
    def __init__(self, nome, cpf, email, data_nascimento, telefone, endereco_entrega, senha, id):
        super().__init__(nome, cpf, email, data_nascimento, telefone, endereco_entrega)
        self.__senha = senha
        self.__id = id

    @property
    def _senha(self):
        return self.__senha

    @_senha.setter
    def _senha(self, value):
        self.__senha = value  

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value    

    def listar(self):
        print(f"Funcionário: {self._nome}, ID: {self._id}, CPF: {self._cpf}, Email: {self._email}, Telefone: {self._telefone}, Data de nascimento: {self._data_nascimento}")
