dicionario_principal = {
    "livro1": {
        "titulo": "A culpa é das estrelas",
        "autor": "John Green",
        "genero": "Romance",
        "ano_publicacao": "2012",
        "idioma": "português",
        "imagem" : "img/aculpaedasestrelas.jpg"
    },
    "livro2": {
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J. K. Rowling",
        "genero": "Fantasia",
        "ano_publicacao": "1997",
        "idioma": "português",
        "imagem" : "img/harrypotter.jpg"
    },
    "livro3": {
        "titulo": "It - A Coisa",
        "autor": "Stephen King",
        "genero": "Terror",
        "ano_publicacao": "1996",
        "idioma": "português",
        "imagem" : "img/itacoisa.jpg"
    },
    "livro4": {
        "titulo": "Jogos Vorazes",
        "autor": "Suzanne Collins",
        "genero": "Distopia",
        "ano_publicacao": "2008",
        "idioma": "português",
        "imagem" : "img/jogosvorazes.jpg"
    },
    "livro5": {
        "titulo": "A Garota no Trem",
        "autor": "Paula Hawkins",
        "genero": "Mistério",
        "ano_publicacao": "2015",
        "idioma": "português",
        "imagem" : "img/agarotanotrem.jpg"
    },
    "livro6": {
        "titulo": "Becoming",
        "autor": "Michelle Obama",
        "genero": "Biografia",
        "ano_publicacao": "2018",
        "idioma": "inglês",
        "imagem" : "img/becoming.jpg"
    },
    "livro7": {
        "titulo": "Os Sete Maridos de Evelyn Hugo",
        "autor": "Taylor Jenkins Reid",
        "genero": "Ficção",
        "ano_publicacao": "2017",
        "idioma": "português",
        "imagem" : "img/ossetemaridos.jpg"
    },
    "livro8": {
        "titulo": "O Silmarillion",
        "autor": "J. R. R. Tolkien",
        "genero": "Fantasia",
        "ano_publicacao": "1997",
        "idioma": "português",
        "imagem" : "img/silmarillion.jpg"
    },
    "livro9": {
        "titulo": "Mil Beijos de Garoto",
        "autor": "Tillie Cole",
        "genero": "Romance",
        "ano_publicacao": "2016",
        "idioma": "português",
        "imagem" : "img/milbeijosdegaroto.jpg"
    },
    "livro10": {
        "titulo": "O Homem de Giz",
        "autor": "C. J. Tudo",
        "genero": "Suspense",
        "ano_publicacao": "2018",
        "idioma": "português",
        "imagem" : "img/ohomemdegiz.jpg"
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



def obter_lista_generos(dicionario):
    # Inicializando uma lista vazia para coletar os gêneros
    lista_generos = []

    # Iterando sobre cada item no dicionário fornecido
    for isbn, detalhes in dicionario.items():
        # Adicionando o gênero do item atual à lista
        lista_generos.append(detalhes['genero'])

    # Convertendo a lista em um conjunto para eliminar duplicatas, e depois de volta a uma lista
    lista_generos_unicos = list(set(lista_generos))

    # Retornando a lista de gêneros únicos
    return lista_generos_unicos

# Exemplo de uso:
# lista_generos_unicos = obter_lista_generos(dicionario_principal)
# print(lista_generos_unicos)
