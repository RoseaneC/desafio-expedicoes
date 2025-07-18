# Desafio Técnico - Análise e Manipulação de Dados em SQLite e Python

[![Python](https://img.shields.io/badge/python-3.13-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3.37.2-lightgrey?logo=sqlite&style=for-the-badge)](https://www.sqlite.org/index.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

Olá! Eu sou **Roseane Carreiro** e este é meu repositório para o desafio técnico sobre banco de dados SQLite e Python.

> ⚠️ **Aviso:** Sou iniciante nessa área. Fiz o desafio pesquisando, tentando entender como funcionava e me esforçando para aprender.

---

## Sobre o desafio

Recebi uma base de dados chamada `expedicoes.db` que simula a operação de um laboratório de pesquisas ambientais. Ela contém informações sobre:

- Expedições científicas
- Pesquisadores participantes
- Locais de coleta
- Equipamentos utilizados
- Amostras coletadas
- Uso dos equipamentos nas expedições
- Participação dos pesquisadores nas expedições

---

## Tabelas principais no banco de dados

| Tabela              | Descrição                               |
|---------------------|---------------------------------------|
| `Expedicoes`        | Expedições realizadas                  |
| `Pesquisadores`     | Pesquisadores participantes           |
| `Locais`            | Locais de coleta                      |
| `Equipamentos`      | Equipamentos utilizados                |
| `Amostras`          | Amostras coletadas                     |
| `UsoEquipamento`    | Uso dos equipamentos nas expedições   |
| `ExpedicaoPesquisador` | Participação de pesquisadores nas expedições |

---

## Tarefas realizadas

1. **Consulta SQL**: Quais equipamentos estão disponíveis para uso?  
   Retorna todos os equipamentos cujo status seja "Disponível".

2. **Consulta SQL**: Qual especialidade foi mais usada em expedições?  
   Identifica a especialidade de pesquisador que mais participou das expedições, considerando os registros de amostras coletadas.

3. **Python & SQL**: Inserção de uma nova expedição com papéis definidos  
   - Insere uma nova expedição com local, datas, equipamentos, amostras, pesquisadores e seus papéis.  
   - Cria registros novos somente se não existirem (evita duplicação).  
   - Mantém integridade referencial entre tabelas.

---

## Como rodar o projeto

1. Garanta que tenha Python 3 instalado (recomendo a versão 3.13).  
2. Instale as dependências com:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Execute o script para criar os dados:  
   ```bash
   python criar_dados.py
   ```  
4. Execute o script principal para ver as consultas:  
   ```bash
   python main.py
   ```  
5. Para inserir a nova expedição, rode:  
   ```bash
   python inserir_expedicao.py
   ```  

---

## Aprendizados

- Aprendi a usar SQLite para consultas e manipulação de dados.  
- Usei Python para interagir com o banco, criando registros e evitando duplicação.  
- Entendi melhor a importância de relacionar tabelas via IDs.  
- Desenvolvi lógica para resolver problemas práticos no banco de dados.

---

## Contato

Se quiser trocar uma ideia ou dar um feedback, me encontre no LINKEDIN:  
[https://www.linkedin.com/in/roseane-carreiro/](https://www.linkedin.com/in/roseane-carreiro/)

---

Obrigado por ler! 🌟
