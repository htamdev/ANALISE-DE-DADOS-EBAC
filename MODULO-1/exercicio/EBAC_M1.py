print('Olá! Digite suas informações pessoais para continuar!\n')

lista_cli = {}  # Inicia a lista

nome_usuario = input('Digite o primeiro nome: ')
sobrenome_usuario = input('Digite seu sobrenome: ')

# Loop para validar a idade
while True:
    try:
        idade_usuario = int(input('Qual é a sua idade? '))
        if idade_usuario >= 0:
            break  # Se número é válido, sai do loop
        else:
            print('A idade não pode ser negativa! Tente novamente.')
    except ValueError:
        print('Erro! Digite um número inteiro válido para a idade.')

email_usuario = input('Qual o seu melhor email válido? ')
cidade_usuario = input('Em qual cidade você reside? ')
estado_usuario = input('Em qual estado você mora? ')
pais_usuario = input('Em qual país você reside? ')

# Adiciona informações ao dicionário
lista_cli['Nome'] = nome_usuario
lista_cli['Sobrenome'] = sobrenome_usuario
lista_cli['Idade'] = idade_usuario
lista_cli['Email'] = email_usuario
lista_cli['Cidade'] = cidade_usuario
lista_cli['Estado'] = estado_usuario
lista_cli['País'] = pais_usuario

# Verifica se todos os valores foram preenchidos corretamente
if all(value.strip() for value in lista_cli.values() if isinstance(value, str)):
    print('Usuário cadastrado com sucesso!')
else:
    print('Por favor, forneça todos os dados solicitados!')

print('\nDados do usuário:')
print('')
print(lista_cli)

# --- Cálculo de Idade ---
print("\nAgora, vamos verificar a diferença de idade entre você e outra pessoa.\n")

# Loop que valida a segunda idade
while True:
    try:
        idade_outro = int(input("Digite a idade de outra pessoa para comparar: "))
        if idade_outro >= 0:
            break  # Se válido, sai do loop
        else:
            print('A idade não pode ser negativa! Tente novamente.')
    except ValueError:
        print('Erro! Digite um número inteiro válido para a idade.')

# Cálculos matemáticos
diferenca = abs(idade_usuario - idade_outro)  # Diferença absoluta
soma = idade_usuario + idade_outro  # Soma das idades
media = (idade_usuario + idade_outro) / 2  # Média das idades
multiplicacao = idade_usuario * idade_outro  # Multiplicação das idades

# Exibe os resultados das operações
# Utilizando 'print(f' para eficiência e formatação
print(f"\n{nome_usuario}, veja os cálculos baseados nas idades fornecidas:")
print(f"- Diferença de idade: {diferenca} anos.")
print(f"- Soma das idades: {soma} anos.")
print(f"- Média das idades: {media:.2f} anos.")
print(f"- Multiplicação das idades: {multiplicacao}.")

# Compara as idades
if idade_usuario > idade_outro:
    print('')
    print("\nVocê é mais velho.")
elif idade_usuario < idade_outro:
    print('')
    print("\nVocê é mais novo.")
else:
    print('')
    print("\nVocês têm a mesma idade.")
