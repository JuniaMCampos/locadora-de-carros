import os

print("===============================")
print("Bem vindo à Locadora de Carros!")
print("===============================")

veiculos = {
    "[0]" : "Chevrolet Tracker - R$ 120 /dia",
    "[1]" : "Chevrolet Onix - R$ 90 /dia",
    "[2]" : "Chevrolet Spin - R$ 150 /dia",
    "[3]" : " Hyundai HB20 - R$ 185 /dia",
    "[4]" : "Hyundai Tucson - R$ 120 /dia",
    "[5]" : "Fiat Uno - R$ 60 /dia",
    "[6]" : "Fiat Mobi - R$ 70 /dia",
    "[7]" : "Fiat Pulse - R$ 130 /dia"
}

carros_alugados = []

while True:
    os.system('cls')

    print("O que deseja fazer?")

    print("0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro")

    escolha = int((input()))

    if escolha == 0:
        i = 0
        for ve, name in veiculos.items():
            print(i, ":", name)
            i += 1
    
    elif escolha == 1:
        print("[ALUGAR] Dê uma olhada em nosso portifólio.")
        i = 0
        for ve, name in veiculos.items():
            print(i, ":", name)
            i += 1
        print("==============================================")
        print("Escolha o código do carro: ")
        ve = int(input())
        ve_string = list(veiculos.keys())[ve]
        name = veiculos[ve_string].split(" - ")[0]
        
        valor_diaria_texto = veiculos[ve_string].split(" - ")[1].replace(" R$ ", "").replace(" /dia", "")
        if valor_diaria_texto.startswith("R$"):
            valor_diaria_texto = valor_diaria_texto[2:]

        valor_diaria = float(valor_diaria_texto)  

        print("Escolha por quantos dias deseja alugar: ")
        dias = int(input())

        custo_total = valor_diaria * dias
        print("Você escolheu o {} por {} dias".format(name, dias))
        print("")
        print("O aluguel totalizaria R$ {}. Deseja alugar? 0 - SIM | 1- NÃO".format(custo_total))
        
        decisao = int(input())
        if decisao == 0:
            print("")
            print("Parabéns, você alugou o {} por {} dias.".format(name, dias))

        #Para remover o carro escolhido da lista de carros para alugar
        carro_alugado = {"nome": name, "dias": dias, "custo_total": custo_total}
        carros_alugados.append(carro_alugado)
        del veiculos[ve_string]


    elif escolha == 2:
        print("Segue lista de carros alugados.")
        if carros_alugados:
            for index, carro in enumerate(carros_alugados):
                print(f"{index}: {carro['nome']} - {carro['dias']} dias - R$ {carro['custo_total']}")
            
            print("Qual você deseja devolver? ")
            carro_devolver = int(input())

            if 0 <= carro_devolver < len(carros_alugados):
                carro_devolvido = carros_alugados.pop(carro_devolver)
                veiculos[len(veiculos)] = "{} - R$ {} /dia".format(carro_devolvido["nome"], valor_diaria)
                print("Carro devolvido com sucesso.")

    print("==================================================")  
    print("0 - CONTINUAR | 1- SAIR") 

    comando = int(input())
    if comando == 1:
        break

    
