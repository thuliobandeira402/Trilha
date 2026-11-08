class Funcionario():
    def __init__(self, nome, salario_base, cargo):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, cargo, bonus):
        super().__init__(nome, salario_base, cargo)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, cargo, comissao):
        super().__init__(nome, salario_base, cargo)
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_base + self.comissao

gerente = Gerente("João", 5000, "Gerente", 1000)
vendedor = Vendedor("Maria", 3000, "Vendedor", 500)

print(f"Salário do gerente {gerente.nome}: R${gerente.calcular_salario()}")
print(f"Salário do vendedor {vendedor.nome}: R${vendedor.calcular_salario()}")
        