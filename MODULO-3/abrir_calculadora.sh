#!/bin/bash

# Verifica se o python3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "Erro: Python3 não está instalado. Por favor, instale o Python3."
    echo "Verifique o arquivo README.md em caso de dúvidas."
    exit 1
fi

# Verifica se o arquivo .py existe no diretório
if [ ! -f "calculadora.py" ]; then
    echo "Erro: O arquivo calculadora.py não foi encontrado no diretório."
    exit 1
fi
# Exibe a mensagem de "timeout" e espera por 3 segundos
echo "Iniciando a calculadora..."
sleep 3  # Tempo em segundos (3 segundos neste caso)

# Executa o script Python
python3 calculadora.py
