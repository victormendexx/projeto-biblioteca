# e2123-e2-seniors
repositório do grupo seniors para a nossa primeira atividade preparatória para o TCC.
# Desafio: Biblioteca Virtual para Empréstimos de Livros Digitais
## Objetivo:
Desenvolver uma aplicação web utilizando Django que simule uma biblioteca virtual para empréstimos de livros digitais. A aplicação deverá permitir que os usuários possam visualizar, emprestar e devolver livros digitais.
## Requisitos:
   - python v-3.10.12
   - django v-3.8

## Banco de dados:
   - Para visualizar os usuários criados no nosso registro, utilize a seguinte url "http://127.0.0.1:8000/admin/".
   - OBS: o login para ver o conteúdo da url acima deve ser feito da seguinte forma no terminal.
   - python manage.py createsuperuser
   - Após este comando você deverá escolher um username e uma senha (recomendamos usar "admin" para os dois). Vale lembrar que o e-mail deve ficar em branco.

## Comandos para executar antes de rodar a página:
   - python3 -m venv venv
   - pip install django
   - cd projeto
   - python manage.py makemigrations
   - python manage.py migrate
   - OBS: após executarem esses comandos você pode utilizar o python manage.py runserver para rodar a página django.
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
   - Permitir que os usuários possam filtrar os livros por título.
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
### - Daily 25/10/2023:
### O que fizemos ontem?
   - Fizemos a barra de pesquisa ser funcional, adicionamos um filtro ao catálogo e fizemos as páginas dos livros.

### O que faremos hoje?
   - Colocaremos css nas páginas dos livros, adicionaremos a função de pedir empréstimo e colocaremos os pdfs dos livros nas páginas dos respectivos.

### O que está nos impedindo?
   
---------------------------------------------------------------------------------------------------------------------------
### - Daily 26/10/2023:
### O que fizemos ontem?
   - Ontem criamos o sistema de empréstimos de livros e o registro do usuário no site.

### O que faremos hoje?
   - Hoje a princípio iremos apresentar o nosso projeto feito.

### O que está nos impedindo?

---------------------------------------------------------------------------------------------------------------------------
### - Daily 06/11/2023:
   -A daily foi feita com o professor
---------------------------------------------------------------------------------------------------------------------------
### - Daily 08/11/2023:
### O que fizemos ontem?
   -
### O que faremos hoje?
   -Relacionamos a tabela e alguns projetos foram conferidos e corrigidos

 ### O que está nos impedindo?

---------------------------------------------------------------------------------------------------------------------------
### - Daily 09/11/2023:
### O que fizemos ontem?
   -Ontem foi conferido os projetos e relacionamos a tabela
### O que faremos hoje?
   -Hoje fizemos uma tabela no admin para avaliaçãoes e adicionamos uma propriedade para calcular a media das avaliações
### O que está nos impedindo?

---------------------------------------------------------------------------------------------------------------------------
### Integrantes da equipe:
   - Ryan W.
   - Isabela R.
   - Bernardo F.
   - Ana Alice
   - Victor G.


# 1 criar a entrada logout no nav
# 2 buscar quais configuracoes de login_url no settings.py
# 3 




# Avaliação por parte do grupo 3 - Entra21

Instalação: 20/20
Avaliação do arquivo README.md: 20/20
Funcionalidades em tela apresentadas e com erros: 20/20
Funcionalidades apresentadas em tela e incompleta sem a devida marcação: 18/20
Percentual de aderência ao enunciado da questão: 20/20


## Nota final: 98/100

### Justificativas: 

Filtro de busca não atende aos requisitos definidos no README, "Permitir que os usuários possam filtrar os livros por título, autor ou status." filtro apenas funciona para gênero e busca para título, incluindo acentos. 


## Checklist:
Modelagem de Dados: Ok
Visualização de Livros: Ok
Empréstimo de Livros: Ok
Devolução de Livros: Ok
Interface Amigável: Ok
Página de Detalhes do Livro: Ok


## Avaliadores:
Fabio Henrique 
Cristina Siewert Jansen
Daianna Marques
Guilherme Zago