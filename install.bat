@echo off
echo Verificando se o Python está instalado...
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python não encontrado. Por favor, instale o Python 3.x manualmente.
    echo Após a instalação do Python, execute o arquivo PontoMagico.py.
    pause
    start https://www.python.org/downloads/
    exit
)
echo Python encontrado. Instalando bibliotecas necessárias...
python -m pip install pandas click
echo Bibliotecas instaladas. Executando o install_dependencies.bat...
call install_dependencies.bat
echo Todas as dependências foram instaladas. Executando o PontoMagico...
start "" python PontoMagico.py
