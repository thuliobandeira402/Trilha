def calculo_salario(horas_trabalhadas, valor_hora):
    salario = horas_trabalhadas * valor_hora
    return salario

number = int(input(""))
valor_hora = float(input(""))
horas_trabalhadas = float(input(""))

print(f"NUMBER = {number}")
print(f"SALARY = U$ {calculo_salario(horas_trabalhadas=horas_trabalhadas, valor_hora=valor_hora):.2f}")