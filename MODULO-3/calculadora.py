def menu():
    print("\n===== CALCULADORA =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    print("======================")

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro! Digite um número válido.")

def calcular():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "5":
            print("\nSaindo da calculadora...")
            break
        
        if opcao not in ["1", "2", "3", "4"]:
            print("\nOpção inválida! Tente novamente.")
            continue
        
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")
        
        if opcao == "1":
            resultado = num1 + num2
            print(f"\nResultado da soma: {resultado}")
        elif opcao == "2":
            resultado = num1 - num2
            print(f"\nResultado da subtração: {resultado}")
        elif opcao == "3":
            resultado = num1 * num2
            print(f"\nResultado da multiplicação: {resultado}")
        elif opcao == "4":
            if num2 == 0:
                print("\nErro! Não é possível dividir por zero.")
            else:
                resultado = num1 / num2
                print(f"\nResultado da divisão: {resultado}")

if __name__ == "__main__":
    calcular()
