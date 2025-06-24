# Magic Point 🕒✨

![GitHub](https://img.shields.io/github/license/anderson5g/ponto-magico)
![GitHub last commit](https://img.shields.io/github/last-commit/anderson5g/ponto-magico)

Magic Point é uma ferramenta desenvolvida para simplificar o tratamento de marcações de ponto de funcionários, transformando registros brutos em dados valiosos para análise. 

## Funcionalidades 🚀

- Separação automática de Data e Dia da Semana 
- Divisão inteligente das marcações de ponto (batidas) 
- Limpeza e organização das justificativas 
- Geração de planilha pronta para análise 

## Pré-requisitos 📋

Para utilizar o programa, você deve ter o Python 3.9 ou superior instalado corretamente. Recomenda-se o uso da versão mais recente do Python para melhor compatibilidade com as bibliotecas mais atuais. Você pode baixar a última versão do Python [aqui](https://www.python.org/downloads/).

## Como Usar 📝

1.  **Baixar o Projeto:**
    Clone este repositório para o seu ambiente local ou faça o download do arquivo ZIP.

    ```bash
    git clone [https://github.com/Draken573/Magic-Point.git](https://github.com/Draken573/Magic-Point.git) # Substitua pelo seu link do repositório, se diferente
    cd Magic-Point
    ```

2.  **Configuração do Ambiente Virtual e Instalação de Dependências:**
    É **altamente recomendado** o uso de um ambiente virtual para isolar as dependências do projeto e evitar conflitos com outras instalações Python no seu sistema.

    * **Criar e ativar o ambiente virtual:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate # Para Linux/macOS
        # Ou .\\venv\\Scripts\\activate.bat (Para Windows - Prompt de Comando)
        # Ou .\\venv\\Scripts\\Activate.ps1 (Para Windows - PowerShell)
        ```
        (Substitua `venv` pelo nome que preferir para o seu ambiente virtual).

    * **Instalar dependências de sistema (se necessário):**
        Em sistemas Debian/Ubuntu, se você encontrar erros de compilação relacionados a pacotes como `numpy` ou `pandas`, pode ser necessário instalar as ferramentas de desenvolvimento do Python e outras dependências de compilação:
        ```bash
        sudo apt update
        sudo apt install python3-dev build-essential libssl-dev libffi-dev
        ```

    * **Atualizar `pip`, `setuptools` e `wheel` no ambiente virtual:**
        Garanta que as ferramentas de instalação estejam atualizadas:
        ```bash
        pip install --upgrade pip setuptools wheel
        ```

    * **Instalar as dependências do projeto:**
        ```bash
        pip install -r requirements.txt
        ```

3.  **Execução:**
    Com o ambiente virtual ativado e as dependências instaladas, execute o script principal:
    ```bash
    python PontoMagico.py
    ```

4.  **Entrada de Dados:**
    O programa solicitará o caminho completo da planilha de entrada (.xlsx). Insira o caminho completo ou arraste o arquivo para a janela do terminal.

5.  **Resultados:**
    Após o processamento, uma nova planilha tratada será gerada e salva na pasta `tratamentos`, localizada no diretório do projeto.

## Exemplo de Uso 👁️‍🗨️

Imagine que você possui uma planilha de marcações de ponto chamada `relatorio_ponto.xlsx`. Ao executar o Magic Point e fornecer o caminho desta planilha, o programa irá processá-la e gerar uma nova planilha na pasta `tratamentos`, pronta para análise detalhada.

## Licença 📜

---

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes. 

Feito com 💪 por [Anderson Monteiro](https://github.com/Draken573) 💻