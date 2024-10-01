import os 
os.system("cls || clear ")
from dataclasses import dataclass

quantidade_de_familiares = 1
lista_familiares = []
lista_salario = []
contator = 0


while True:
    
        print("""
            /t === MENU ===
            1 - adiocionar família
            2 - Exibir resultados
            3 - Sair
        
        """)

        resposta = int(input("deseja adicionar mais uma familia? "))

        match resposta:
            case 1:
                    quantidade_filhos = int(input("digite a sua quantidade de filhos: "))
                    salario = float(input("digite seu salario: "))
                    
                    contator += 1
                    lista_familiares.append(quantidade_filhos)
                    lista_salario.append(salario)
                
            case 2:
                maiorsalario =max(lista_salario)
                menorsalario =min(lista_salario)
                print("maior salario: {maiorsalario}")
                print("menor salario: {menorsalario}")
                print("quantidade de filhos: {quantidade_filhos}")
                print("total de familiares que responderam a pesquisa {contador}")
                break
            case 3:
                print("===programa finalizado===")
                break    
            case _:
                print("opção invalida")


