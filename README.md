# Método Baseado no Reconhecimento de Expressões Emocionais, Comportamentos e Objetos para Monitoramento de Segurança em Ambientes Educacionais

## Descrição

Este repositório contém o projeto desenvolvido como parte da dissertação de Reginaldo Donizeti Cândido, que propõe um método inovador, denominado MMS-EDU, para monitoramento de segurança em ambientes educacionais. O método utiliza reconhecimento de expressões emocionais, análise de comportamentos e objetos para identificar situações de risco.

## Objetivo

O objetivo principal deste projeto é fornecer uma ferramenta que ajude educadores e profissionais de segurança a monitorar e avaliar o comportamento dos alunos, promovendo um ambiente escolar mais seguro.

## Principais Tópicos da Dissertação

1. **Introdução ao MMS-EDU**
   - Apresentação do método e sua importância para a segurança em ambientes educacionais.

2. **Reconhecimento de Expressões Emocionais**
   - Análise comparativa de softwares de reconhecimento de emoções e sua aplicação no contexto educacional.

3. **Calculadora de Ranking SMI**
   - Implementação de uma calculadora que avalia o Índice de Medida de Situação (SMI) com base em dados de diferentes dimensões (EE, SB, SO).

4. **Simulações e Resultados**
   - Descrição das simulações realizadas para validar o método e os resultados obtidos.

5. **Discussão e Conclusões**
   - Reflexões sobre as implicações dos resultados e sugestões para trabalhos futuros.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:
```bash
/calculadora_smi
│
├── entradas/          # Arquivos de entrada (CSV)
│   ├── EE.csv
│   ├── SB.csv
│   ├── SO.csv
│   ├── Relevancia.csv
│   └── Alunos.csv
│
├── saidas/             # Arquivos de saída
│   └── resultados.csv
│
├── calculadora_msi.py           # Código principal da calculadora SMI
└── README.md                    # Este arquivo
````
## Como Usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/reginaldocandido/MMS-EDU.git
   cd seu_repositorio/calculadora_smi

1. Instale as dependências:
Certifique-se de ter o Python e o Pandas instalados. Você pode instalar as dependências necessárias com:

pip install pandas
pip install openpyxl

2. Prepare os arquivos de entrada:

- Certifique-se de que os arquivos CSV estão corretamente formatados e localizados na pasta entradas/.

3. Execute a calculadora:

python calculadora_msi.py

4. Resultados:

- Os resultados serão salvos na pasta saidas/ como Ranking_SMI_MMS-EDU.xlsx.

Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

Licença

Este projeto está licenciado sob a 
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
Veja o arquivo LICENSE para mais detalhes.

Contato

Para mais informações, entre em contato com Reginaldo Donizeti Cândido através do e-mail: reginaldo.candido@etec.sp.gov.br.

Sinta-se à vontade para personalizar o conteúdo, como o nome do repos
