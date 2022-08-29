def retorna_triangulo(lado1, lado2, lado3):
    ver = []

    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        ver.append(True)
    else:
        ver.append(False)

    if False not in ver:
        count_iguais = 0
        if lado1 == lado2:
            count_iguais += 1
        if lado1 == lado3:
            count_iguais += 1
        if lado2 == lado3:
            count_iguais += 1
        if count_iguais == 0:
            return "É um triângulo Escaleno!"
        elif count_iguais == 1:
            return "É um triângulo Isóceles"
        else:
            return "É um triângulo Equilátero"
    else:
        return "Não é um triângulo!"


while True:
    lado_1 = float(input("Digite o primeiro lado do triângulo: "))
    while lado_1 < 0:
        print("Opção inválida!")
        lado_1 = float(input("Digite o primeiro lado do triângulo: "))

    lado_2 = float(input("Digite o segundo lado do triângulo: "))
    while lado_2 < 0:
        print("Opção inválida!")
        lado_2 = float(input("Digite o segundo lado do triângulo: "))
    lado_3 = float(input("Digite o terceiro lado do triângulo: "))

    while lado_3 < 0:
        print("Opção inválida!")
        lado_3 = float(input("Digite o terceiro lado do triângulo: "))
    print(retorna_triangulo(lado_1, lado_2, lado_3))

    continuar = int(input("Deseja continuar?(1 - Sim / 2 - Não) "))
    while continuar != 1 and continuar != 2:
        print("Opção inválida!")
        continuar = int(input("Deseja continuar?(1 - Sim / 2 - Não) "))
    if continuar == 2:
        break

print("Você saiu!")
