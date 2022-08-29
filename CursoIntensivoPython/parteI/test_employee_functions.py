import unittest
from employee_functions import Employee

class TestCriaFuncionario(unittest.TestCase):
    """Testes para a classe Employee"""
    
    def setUp(self):
        self.aumento = 7520
        self.empregado = Employee('fabio','mascarenhas',120000)
        
    def test_give_default_raise(self):
        """Teste de aumento de salario padrao"""
        self.empregado.give_raise()
        self.assertEqual(self.empregado.salario_anual,125000)

    def test_give_custom_raise(self):
        """Teste de aumento de salario customizado"""
        self.empregado.give_raise(self.aumento)
        self.assertEqual(self.empregado.salario_anual,127520)

unittest.main()