class Employee():
    """Representação de um funcionário"""

    def __init__(self,nome,sobrenome,salario_anual):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_anual = salario_anual

    def give_raise(self,valor=5000):
        self.salario_anual += valor