''''''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
valor4 = int(input("Digite o quarto valor: "))
soma = valor1 + valor2 + valor3 + valor4
multiplicacao = valor1 * valor2 * valor3 * valor4
print("Resultado da adição:", soma)
print("Resultado da multiplicação:", multiplicacao)
valor_em_dolares = float(input("Digite o valor em Dolares:" ))
valor_em_reais = valor_em_dolares * 3.80
print(f"{valor_em_dolares} Dolares equivalem a {valor_em_reais:.2f} Reais. ")