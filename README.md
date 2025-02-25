# Calculadora de Ranking SMI para o Método MMS-EDU

Este repositório contém o código-fonte da Calculadora de Ranking SMI, uma ferramenta desenvolvida como parte da dissertação de mestrado "Um Método Baseado no Reconhecimento de Expressões Emocionais, Comportamentos e Objetos para Monitoramento de Segurança em Ambientes Educacionais". A calculadora implementa o Índice de Monitoramento de Segurança (SMI) proposto no método MMS-EDU.

## Descrição

A Calculadora de Ranking SMI é uma aplicação Python que permite simular o monitoramento de segurança em ambientes escolares, com base em três dimensões:

*   **Expressões Emocionais (EE):** Detectadas por meio de algoritmos de reconhecimento facial.
*   **Comportamentos Suspeitos (SB):** Identificados por meio de análise de vídeo.
*   **Objetos Suspeitos (SO):** Detectados por meio de algoritmos de detecção de objetos.

A calculadora recebe dados de entrada (simulados ou provenientes de sistemas de visão computacional), aplica a equação do SMI e gera um ranking de indivíduos com base no seu nível de risco potencial.

## Estrutura do Repositório
- **`calculadora_smi.py`**: Código principal da calculadora, que processa os arquivos CSV de entrada e calcula o SMI.
- **`interface_simulacao.py`**: Código da interface gráfica para simulação, que permite inserir dados manualmente e visualizar os resultados.
- **`entradas/`**: Pasta contendo os arquivos CSV de entrada (exemplos):
  - `Alunos.csv`: Dados dos alunos (ID e nome).
  - `EE.csv`: Dados de expressões emocionais.
  - `SB.csv`: Dados de comportamentos suspeitos.
  - `SO.csv`: Dados de objetos suspeitos.
  - `Relevancia.csv`: Fatores de relevância.
  - `Riscos.csv`: Tabela de mapeamento de riscos.
- **`saidas/`**: Pasta onde são salvos os resultados (arquivos Excel).
- **`requirements.txt`**: Lista de bibliotecas Python necessárias, com suas versões.
- **`assets/`**: Contém o ícone da aplicação.
- **`README.md`**: Este arquivo, que fornece informações sobre o projeto.

## Pré-requisitos

*   Python 3.7 ou superior.
*   Bibliotecas Python listadas no arquivo `requirements.txt`.

## Instalação e Configuração

1.  **Clone este repositório:**
    ```bash
    git clone <URL do repositório>
    ```
2.  **Crie um ambiente virtual Python (recomendado):**
    ```bash
    python3 -m venv venv  # Ou python -m venv venv, dependendo do seu sistema
    ```
3.  **Ative o ambiente virtual:**
    ```bash
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No Linux/macOS
    ```
4.  **Instale as bibliotecas necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

## Execução

### Usando a Interface Gráfica (Recomendado para Simulações)

1.  Execute o script `interface_simulacao.py`:
    ```bash
    python interface_simulacao.py
    ```
2.  Insira os dados na interface gráfica (ou carregue um arquivo CSV de exemplo).
3.  Clique em "Salvar e Executar".
4.  Os resultados serão salvos em um arquivo Excel na pasta `saidas/`.

### Usando a Linha de Comando (Para Processar Arquivos CSV)

1.  Certifique-se de que os arquivos CSV de entrada estejam na pasta `entradas/`.
2.  Execute o script `calculadora_smi.py`:
    ```bash
    python calculadora_smi.py
    ```
3.  Os resultados serão salvos em um arquivo Excel na pasta `saidas/`.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão, por favor, abra uma *issue* ou envie um *pull request*.


## Licença

Este projeto está licenciado sob a 
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
Veja o arquivo LICENSE para mais detalhes.

## Contato

Para mais informações, entre em contato com Reginaldo Donizeti Cândido através do e-mail: reginaldo.candido@etec.sp.gov.br.
