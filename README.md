# Organizador de Estudos

Sistema de linha de comando para organizar atividades acadêmicas com priorização automática baseada em prazo, peso da atividade e nível de confiança do estudante.

## O que o sistema faz

Você cadastra suas matérias e atividades pendentes informando a data limite, o quanto a atividade vale e o quanto você já domina o conteúdo. O sistema calcula automaticamente uma pontuação de urgência para cada atividade e te mostra a lista ordenada do mais urgente pro menos urgente, ajudando a decidir o que estudar primeiro.

## Como a priorização funciona

A urgência de cada atividade é calculada pela fórmula:

urgencia = (peso * (10 - confianca)) / dias_restantes

Atividades com prazo já vencido recebem urgência máxima automaticamente.

## Tecnologias utilizadas

- Python 3
- PostgreSQL 18
- pg8000
- python-dotenv

## Como rodar o projeto

Clone o repositório e crie um arquivo .env na raiz com base no .env.example:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=postgres
DB_PASSWORD=sua_senha

Instale as dependências:

pip install pg8000 python-dotenv

Crie as tabelas no PostgreSQL:

CREATE TABLE IF NOT EXISTS materias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    confianca_geral INTEGER
);

CREATE TABLE IF NOT EXISTS atividades (
    id SERIAL PRIMARY KEY,
    materia_id INTEGER REFERENCES materias(id),
    titulo VARCHAR(200) NOT NULL,
    data_limite DATE NOT NULL,
    peso INTEGER NOT NULL,
    confianca INTEGER CHECK (confianca BETWEEN 0 AND 10),
    horario TIME,
    status VARCHAR(20) DEFAULT 'pendente'
);

Execute o programa:

python main.py

## Funcionalidades

- Cadastro de matérias com nível de confiança geral
- Cadastro de atividades com prazo, peso, confiança e horário
- Listagem de atividades pendentes ordenadas por urgência
- Marcar atividade como concluída

## Autor

Brenno Gomes
