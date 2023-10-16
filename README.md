# e2123-e2-seniors
repositório do grupo seniors para a nossa primeira atividade preparatória para o TCC.
# Desafio: Biblioteca Virtual para Empréstimos de Livros Digitais
## Objetivo:
Desenvolver uma aplicação web utilizando Django que simule uma biblioteca virtual para empréstimos de livros digitais. A aplicação deverá permitir que os usuários possam visualizar, emprestar e devolver livros digitais.
## Requisitos:
   - python v-3.10.12
   - django v-3.8
### 1. Modelagem de Dados:
   - Cada livro digital será representado por um dicionário com as seguintes informações: título, autor, editora, ano de publicação e status (disponível ou emprestado).
   - Os dicionários de livros serão armazenados em uma estrutura de dados adequada para facilitar as operações CRUD (por exemplo, uma lista de dicionários).
```python
publicacoes = [
    {
        'id': 1,
        'titulo': 'Meu Primeiro Amor',
        'autor': 'Autor Desconhecido',
        'editora': 'Editora ABC',
        'ano_publicacao': 2020,
        'status': 'disponivel'  # Ou 'emprestado'
    },
    # Outros livros aqui...
]
```
### 2. Visualização de Livros:
   - Implementar uma página que liste todos os livros disponíveis na biblioteca virtual, mostrando suas informações básicas.
   - Permitir que os usuários possam filtrar os livros por título, autor ou status.
### 3. Empréstimo de Livros:
   - Implementar uma funcionalidade que permita aos usuários emprestar um livro. Ao emprestar um livro, o status do livro deve mudar para "emprestado".
```python
livro_emprestado = {
    'id': 1,
    'titulo': 'Meu Primeiro Amor',
    'autor': 'Autor Desconhecido',
    'editora': 'Editora ABC',
    'ano_publicacao': 2020,
    'status': 'emprestado'
}
```
   - Certificar que um livro que já foi emprestado não possa ser emprestado novamente até que seja devolvido.
### 4. Devolução de Livros:
   - Implementar uma funcionalidade que permita aos usuários devolver um livro. Ao devolver um livro, o status do livro deve mudar para "disponível".
### 5. Interface Amigável:
   - Criar uma interface amigável e intuitiva para facilitar a interação dos usuários com a aplicação.
### 6. Página de Detalhes do Livro:
   - Implementar uma página de detalhes para cada livro, onde os usuários possam ver informações mais detalhadas sobre o livro e seu status atual.
## Desafios Adicionais:
### - Sistema de Contas de Usuário (Sem persistência de dados):
   - Criar um sistema simples de contas de usuário onde os usuários possam fazer login com um nome de usuário.
   - Rastrear quais livros estão emprestados para cada usuário.
### - Histórico de Empréstimos:
   - Implementar uma funcionalidade que permita aos usuários visualizar um histórico de todos os livros que eles emprestaram e devolveram.
Lembre-se de que, para implementar esta aplicação, você precisará do framework Django e deve seguir as melhores práticas de desenvolvimento web para garantir a segurança e a eficiência da aplicação. Boa sorte!
---------------------------------------------------------------------------------------------------------------------------
### - Daily 11/10/2023:
### O que fizemos ontem?
   - Ontem o intuito da aula foi mais para explicar o uso do git no nosso projeto, vimos sobre os comandos gits que usaremos para fazer o merge, as branchs, e etc.

### O que faremos hoje?
   - Hoje começaremos a falar mais sobre o projeto em si
   - Planejar os menus e layout
   - Distribuição de tarefas.

### O que está nos impedindo?
   - Atualmente o que está nos impedindo é a impossibilidade de alguns alunos de comparecerem a aula. 
   - ISSO NAO PODE APARECER AQUI
---------------------------------------------------------------------------------------------------------------------------
### - Daily 18/10/2023:
### O que fizemos ontem?
   - Na ultima aula criamos o projeto do Django com os principais arquivos html. Tambem trabalhamos durante o final de semana estilizando com css.

### O que faremos hoje?
   - O catálogo

### O que está nos impedindo?
   
---------------------------------------------------------------------------------------------------------------------------
### Integrantes da equipe:
   - Ryan W.
   - Isabela R.
   - Bernardo F.
   - Ana Alice
   - Victor G.