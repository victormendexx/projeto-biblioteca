dicionario_principal = {
    1: {
        "titulo": "A culpa é das estrelas",
        "autor": "John Green",
        "genero": "Romance",
        "ano_publicacao": "2012",
        "idioma": "português",
        "imagem" : "img/aculpaedasestrelas.jpg",
        "sinopse": "A Culpa é das Estrelas é um livro emocionante, que trata do amor de dois jovens aprendendo desde cedo a lidar com o fato de que poderão ser afastados um do outro a qualquer momento. Apesar disso, a história de John Green mostra que é possível driblar as dificuldades para alcançar ao menos um pouco de alegria."
    },
    2: {
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J. K. Rowling",
        "genero": "Fantasia",
        "ano_publicacao": "1997",
        "idioma": "português",
        "imagem" : "img/harrypotter.jpg",
        "sinopse": "Descobre sua verdadeira história e seu destino: ser um aprendiz de feiticeiro até o dia em que terá que enfrentar a pior força do mal, o homem que assassinou seus pais. O menino de olhos verde, magricela e desengonçado, tão habituado à rejeição, descobre, também, que é um herói no universo dos magos."

    },
    3: {
        "titulo": "It - A Coisa",
        "autor": "Stephen King",
        "genero": "Terror",
        "ano_publicacao": "1996",
        "idioma": "português",
        "imagem" : "img/itacoisa.jpg",
        "sinopse": "Durante as férias de 1958, em uma pacata cidadezinha chamada Derry, um grupo de sete amigos começa a ver coisas estranhas. Um conta que viu um palhaço, outro que viu uma múmia. Finalmente, acabam descobrindo que estavam todos vendo a mesma coisa: um ser sobrenatural e maligno que pode assumir várias formas."
    },
    4: {
        "titulo": "Jogos Vorazes",
        "autor": "Suzanne Collins",
        "genero": "Distopia",
        "ano_publicacao": "2008",
        "idioma": "português",
        "imagem" : "img/jogosvorazes.jpg",
        "sinopse": "Quando Katniss Everdeen, de 16 anos, decide participar dos Jogos Vorazes para poupar a irmã mais nova, causando grande comoção no país, ela sabe que essa pode ser a sua sentença de morte. Mas a jovem usa toda a sua habilidade de caça e sobrevivência ao ar livre para se manter viva."
    },
    5: {
        "titulo": "A Garota no Trem",
        "autor": "Paula Hawkins",
        "genero": "Mistério",
        "ano_publicacao": "2015",
        "idioma": "português",
        "imagem" : "img/agarotanotrem.jpg",
        "sinopse":"Um thriller psicológico que vai mudar para sempre a maneira como você observa a vida das pessoas ao seu redor. Todas as manhãs Rachel pega o trem das 8h04 de Ashbury para Londres. O arrastar trepidante pelos trilhos faz parte de sua rotina."
    },
    6: {
        "titulo": "Becoming",
        "autor": "Michelle Obama",
        "genero": "Biografia",
        "ano_publicacao": "2018",
        "idioma": "inglês",
        "imagem" : "img/becoming.jpg",
        "sinopse": "Nas suas memórias, uma obra de reflexão profunda e uma narrativa fascinante, Michelle Obama convida os leitores a entrar no seu mundo, relatando as experiências que a moldaram - desde a infância na zona sul de Chicago, passando pelos anos como executiva, equilibrando as exigências da maternidade e o trabalho, até ao tempo passado no endereço mais famoso do mundo..Terno, sábio e revelador, BECOMING é um relato íntimo de uma mulher de alma e substância que desafiou constantemente as expectativas - e cuja história nos inspira a fazer o mesmo."
    },
    7: {
        "titulo": "Os Sete Maridos de Evelyn Hugo",
        "autor": "Taylor Jenkins Reid",
        "genero": "Ficção",
        "ano_publicacao": "2017",
        "idioma": "português",
        "imagem" : "img/ossetemaridos.jpg",
        "sinopse": "Da chegada a Hollywood no início da década de 1950 à decisão de abandonar o mundo do espetáculo 30 anos depois, incluindo, claro está, os seus sete casamentos, a vida de Evelyn é repleta de ambição desmedida, amizades improváveis e um grande amor proibido."
    },
    8: {
        "titulo": "O Silmarillion",
        "autor": "J. R. R. Tolkien",
        "genero": "Fantasia",
        "ano_publicacao": "1997",
        "idioma": "português",
        "imagem" : "img/silmarillion.jpg",
        "sinopse": "Quando o primeiro Senhor das Trevas, Morgoth, rouba as joias e as coloca numa coroa de ferro na impenetrável fortaleza de Angband, Fëanor e os seus familiares pegam em armas contra os deuses e travam uma longa e terrível guerra para recuperá-las."
    },
    9: {
        "titulo": "Mil Beijos de Garoto",
        "autor": "Tillie Cole",
        "genero": "Romance",
        "ano_publicacao": "2016",
        "idioma": "português",
        "imagem" : "img/milbeijosdegaroto.jpg",
        "sinopse": "Quando, aos dezessete anos, Rune Kristiansen retorna da Noruega para o lugar onde passou a infância – a cidade americana de Blossom Grove, na Geórgia –, ele só tem uma coisa em mente: reencontrar Poppy Litchfield, a garota que era sua cara-metade e que tinha prometido esperar fielmente por seu retorno."
    },
    10: {
        "titulo": "O Homem de Giz",
        "autor": "C. J. Tudo",
        "genero": "Suspense",
        "ano_publicacao": "2018",
        "idioma": "português",
        "imagem" : "img/ohomemdegiz.jpg",
        "sinopse": "Assassinato e sinais misteriosos em uma trama para fãs de Stranger Things e Stephen KingEm 1986, Eddie e os amigos passam a maior parte dos dias andando de bicicleta pela pacata vizinhança em busca de aventuras. Os desenhos a giz são seu código secreto: homenzinhos rabiscados no asfalto; mensagens que só eles entendem."
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
