# README - Desafio Técnico SQLite e Python / Technical Challenge SQLite and Python

---

## Sobre o Projeto / About the Project

Este projeto é sobre entender e mexer em um banco de dados SQLite que simula o funcionamento de um laboratório de pesquisas ambientais. Meu objetivo foi aprender a fazer consultas SQL e inserir dados usando Python, mesmo sendo iniciante no assunto.

This project is about understanding and working with a SQLite database that simulates the operations of an environmental research lab. My goal was to learn how to make SQL queries and insert data using Python, even though I’m a beginner in this area.

---

## O que eu consegui fazer / What I managed to do

- Buscar equipamentos que estão disponíveis para uso.  
- Descobrir qual especialidade participou mais das expedições com coleta de amostras.  
- Inserir uma nova expedição no banco, com os pesquisadores e as amostras, usando Python.  
- Tentei garantir que não houvesse dados repetidos ao inserir pesquisadores e relacionar tudo corretamente.  

- Find equipment that is available for use.  
- Find out which specialty participated the most in expeditions with sample collections.  
- Insert a new expedition into the database, with researchers and samples, using Python.  
- Tried to make sure there were no duplicate data when inserting researchers and linking everything correctly.

---

## Limitações e o que não consegui fazer / Limitations and What I Couldn’t Do

Como o banco de dados já veio com um formato definido, não consegui implementar tudo que o desafio pediu, por exemplo:

- Não existe uma tabela separada para "Locais", então o local da expedição fica como texto simples.  
- Não tem uma tabela para registrar o uso dos equipamentos, então não foi possível registrar isso.  
- A tabela de amostras não tem campo para resultados das análises.  
- Também não existe campo para os papéis dos pesquisadores na expedição, então essa parte não foi feita.  

Because the database came with a fixed format, I couldn’t do everything the challenge asked, for example:

- There is no separate table for "Locations", so the expedition location is just plain text.  
- There’s no table to register equipment usage, so I couldn’t add that.  
- The samples table doesn’t have a field for analysis results.  
- There is also no field for the roles of the researchers in the expedition, so I didn’t do that part.

---

## Como usar / How to Use

1. Tenha o Python 3 instalado.  
2. Rode o arquivo `criar_dados.py` para criar o banco e os dados iniciais.  
3. Rode o `main.py` para ver as consultas funcionando.  
4. Rode o `inserir_expedicao.py` para adicionar a nova expedição pelo Python.  

1. Have Python 3 installed.  
2. Run `criar_dados.py` to create the database and initial data.  
3. Run `main.py` to see the queries working.  
4. Run `inserir_expedicao.py` to add the new expedition using Python.

---

## Como o banco está organizado / How the Database Is Organized

| Tabela          | Campos principais                  | O que significa                 |
|-----------------|----------------------------------|-------------------------------|
| Equipamentos    | id, nome, descricao, status      | Equipamentos disponíveis       |
| Pesquisadores   | id, nome, especialidade          | Pessoas que participam          |
| Expedicoes      | id, local (texto), data          | Expedições feitas              |
| Amostras        | id, tipo, expedicao_id           | Amostras coletadas             |
| ExpedicaoPesquisador | id, pesquisador_id, expedicao_id | Liga pesquisadores e expedições|

| Table          | Main fields                      | What it means                  |
|----------------|---------------------------------|-------------------------------|
| Equipamentos    | id, name, description, status   | Available equipment            |
| Pesquisadores   | id, name, specialty             | People who participate        |
| Expedicoes      | id, location (text), date       | Expeditions done              |
| Amostras        | id, type, expedition_id         | Samples collected             |
| ExpedicaoPesquisador | id, researcher_id, expedition_id | Links researchers and expeditions|

---

## Sobre mim / About Me

Meu nome é Roseane Carreiro. Não sou especialista em bancos de dados, mas me dediquei bastante para entender como funciona essa área, pesquisando e testando o que aprendi. Este desafio foi uma ótima oportunidade para praticar e aprender na prática.

My name is Roseane Carreiro. I’m not a database expert, but I worked hard to understand how this area works by researching and testing what I learned. This challenge was a great chance to practice and learn hands-on.

---

## Contato / Contact

- LinkedIn: [https://www.linkedin.com/in/roseane-carreiro/)  
- Email: Roseanecarreirom@gmail.com

---

## Badges

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![SQLite](https://img.shields.io/badge/SQLite-3.39.0-lightgrey?logo=sqlite&logoColor=blue)](https://sqlite.org/)  
[![Status](https://img.shields.io/badge/Status-In%20Progress-orange)](https://github.com/roseanecarreiro/expedicoes)  
