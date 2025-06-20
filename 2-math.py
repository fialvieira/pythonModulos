import math as m

# 1 - Acessar o número PI
print(f"PI: {m.pi:.2f}")

# 2 - Acessar o número de Euler
print(f"Euler: {m.e:.2f}")

# 3 - Arredondamento de números para cima e para baixo
num = 10.4
print(m.ceil(num))      # Arredndamento para cima
print(m.floor(num))     # Arredondamento para baixo

# 4 - Fatorial de um número
num2 = int(input("Digite um número - fatorial: "))
print(m.factorial(num2))

# 5 - Potência de um número
num3 = int(input("Digite um número: "))
pot = int(input("Digite um número - potência: "))
print(f"Número {num3} elevado a {pot} é {m.pow(num3, pot):.2f}")

# 6 - Raiz quadrada de um número
print(m.sqrt(169))

# 7 - MDC (Máximo Divisor Comum)
mdc = m.gcd(20, 100)
print(mdc)

# 8 - Logaritmo
print(m.log(10))