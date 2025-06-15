def calculadora(operacao):
    def somar(a, b):
        return a + b
    
    def multiplicar(a, b):
        return a * b
    
    if operacao == "soma":
        return somar
    elif operacao == "multiplicacao":
        return multiplicar

# Uso:
a = input("escolha soma ou multiplicacao: ")
soma_func = calculadora(a)
resultado = soma_func(5, 3)  # 8

print(resultado)