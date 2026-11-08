# 📌 Gestor de Tarefas Pessoal (Python POO)

Mini-projeto desenvolvido para o módulo de Python, aplicando os conceitos fundamentais de Programação Orientada a Objetos (POO) em uma aplicação de terminal.

---

## 🎯 Problema Resolvido

No dia a dia, a falta de organização e priorização das atividades cotidianas pode levar ao esquecimento de prazos e acúmulo de pendências. 
Para resolver isso, fiz esse miniprojeto que resolve essa questão, fornecendo um sistema simples para gerenciar tarefas pessoais, permitindo:
- Cadastrar tarefas com níveis de prioridade definidos.
- Acompanhar e atualizar o status de cada item (`Pendente`, `Em andamento`, `Concluída`).
- Listar todas as pendências no terminal.
- Garantir o funcionamento correto da plataforma através de validações automáticas, impedindo dados inválidos (ex.: títulos em branco ou prioridades inexistentes).

---

## 🛠️ Conceitos de POO Utilizados

- **Classes e Instâncias:** Temos duas classes, `Tarefa` e `GestorDeTarefas`.
- **Encapsulamento e Proteção de Dados:** Uso de atributos privados (`_titulo`, `_prioridade`, `_status`) associados aos decoradores `@property` e setters para validar as entradas de dados diretamente na atribuição.
- **Tratamento de Exceções:** Lançamento de `ValueError` quando dados fora do padrão esperado são inseridos.

---

## 🚀 Como Executar o Código

### Pré-requisitos
- Ter o **Python 3.x** instalado no sistema.
- Git (opcional, para clonar o repositório).

### Passo a passo

### Passo a passo

1. **Clone o repositório ou baixe o arquivo:**
   ```bash
   git clone [https://github.com/thuliobandeira402/Trilha.git](https://github.com/thuliobandeira402/Trilha.git)
   cd Trilha/Aula3-Python-miniprojeto
   ```

2. **Execute o script pelo terminal:**
   ```bash
   python gestordetarefas.py
   ```

3. **Saída esperada:**
   O programa executará a rotina de demonstração criada, printando a criação das tarefas, a listagem formatada, as alterações de estado e o tratamento das tentativas inválidas capturadas pelos blocos `try/except`.
