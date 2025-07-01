import random

# 1 - Seleciona valor aleatório de uma lista
list1 = [7,6,4,3,2,1]
print(random.choice(list1))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(5, 15)
print(r1)

# 3 - Seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 2 - Seleciona mais de um valor aleatório
# random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "Olá mundo"
print(random.sample(s, 2))

# 5 - Programa de sorteio:
done = False
while not done:
    print("O que você deseja fazer?")
    print("1 - Adivinhar o número")
    print("2 - Sair")
    choice = int(input("> "))
    if choice == 1:
        print("=====Adivinhe um número de 1 a 10=====\n")
        number = int(input("Digite um número entre 1 e 10: "))
        result = random.randint(1, 10)
        if number == result:
            print("Parabêns, você adivinhou corretamente!")
        else:
            print(f"Tente novamente. O número sorteado foi {result}")
    elif choice == 2:
        done = True
    else:
        print("Opção inválida. Digite 1 ou 2.")