dicionario_principal = {
    "978-85-8057-225-4": {
        "titulo": "A culpa é das estrelas",
        "autor": "John Green",
        "genero": "Romance",
        "ano_publicacao": "2012",
        "idioma": "português",
    },
    "978-1-78110-368-5": {
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J. K. Rowling",
        "genero": "Fantasia",
        "ano_publicacao": "1997",
        "idioma": "português",
    },
    "978-85-8105-152-9": {
        "titulo": "It - A Coisa",
        "autor": "Stephen King",
        "genero": "Terror",
        "ano_publicacao": "1996",
        "idioma": "português",
    },
    "978-85-8122-030-7": {
        "titulo": "Jogos Vorazes",
        "autor": "Suzanne Collins",
        "genero": "Distopia",
        "ano_publicacao": "2008",
        "idioma": "português",
    },
    "978-85-01-10541-7": {
        "titulo": "A Garota no Trem",
        "autor": "Paula Hawkins",
        "genero": "Mistério",
        "ano_publicacao": "2015",
        "idioma": "português",
    },
    "978-1-5247-6313-8": {
        "titulo": "Becoming",
        "autor": "Michelle Obama",
        "genero": "Biografia",
        "ano_publicacao": "2018",
        "idioma": "inglês",
    },
    "978-85-5451-368-9": {
        "titulo": "Os Sete Maridos de Evelyn Hugo",
        "autor": "Taylor Jenkins Reid",
        "genero": "Ficção",
        "ano_publicacao": "2017",
        "idioma": "português",
    },
    "978-0-261-10366-5": {
        "titulo": "O Silmarillion",
        "autor": "J. R. R. Tolkien",
        "genero": "Fantasia",
        "ano_publicacao": "1997",
        "idioma": "português",
    },
    "978-14-0595-531-7": {
        "titulo": "Mil Beijos de Garoto",
        "autor": "Tillie Cole",
        "genero": "Romance",
        "ano_publicacao": "2016",
        "idioma": "português",
    },
    "978-85-510-0295-7": {
        "titulo": "O Homem de Giz",
        "autor": "C. J. Tudo",
        "genero": "Suspense",
        "ano_publicacao": "2018",
        "idioma": "português",
    }
}


def filtrar_por_genero(dicionario, genero):
    # Inicializando um dicionário vazio para armazenar os resultados
    dicionario_filtrado = {}

    # Iterando sobre cada item no dicionário fornecido
    for isbn, detalhes in dicionario.items():
        # Verificando se o gênero do item atual corresponde ao gênero desejado
        if detalhes['genero'].lower() == genero.lower():
            # Se corresponder, adicionar o item ao dicionário filtrado
            dicionario_filtrado[isbn] = detalhes

    # Retornando o dicionário filtrado
    return dicionario_filtrado

# Exemplo de uso:
# genero_desejado = 'Romance'
# livros_filtrados = filtrar_por_genero(dicionario_principal, genero_desejado)
# print(livros_filtrados)

