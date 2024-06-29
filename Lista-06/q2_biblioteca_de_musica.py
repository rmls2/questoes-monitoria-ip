#Genero selecionado
genero = input()

albuns = [("Abbey Road", "The Beatles", 1969, "Rock"), 
          ("The Dark Side of the Moon", "Pink Floyd", 1973, "Rock"), 
          ("Riot!", "Paramore", 2007, "Rock"), 
          ("Fearless", "Taylor Swift", 2008, "Pop"), 
          ("Da Lama ao Caos", "Chico Science e Nação Zumbi", 1994, "Rock"), 
          ("Gal Costa", "Gal Costa", 1969, "MPB"),
          ("Sim", "Vanessa da Mata", 2007, "MPB"),
          ("As 20 Melhores", "Luiz Gonzaga", 2004, "Forró"),
          ("O Melhor de Dominguinhos", "Dominguinhos", 2013, "Forró"),
          ("Alucinação", "Belchior", 1976, "MPB"),
          ("Samba Esquema Novo", "Jorge Ben Jor", 1963, "Samba")]


def buscar_album_por_genero(albuns: list, genero: str)-> list:
    """ 
    Busca e retorna uma lista de álbuns que correspondem ao gênero especificado.
    
    Parâmetros:
        - lista_de_albuns: Uma lista de tuplas ou dicionários, onde cada elemento representa um álbum.
        - genero: Uma string representando o gênero musical a ser buscado.
        
    Retorna:
        Uma lista de álbuns que correspondem ao gênero especificado.
    """
    albuns_por_genero = []
    
    for album in albuns:
        genero_album = album[3]
        if genero_album == genero:
            albuns_por_genero.append(album)
        
    if not albuns_por_genero:
        return []
    
    return albuns_por_genero

# se não existir o gênero procurado, vamos add um álbum desse gênero: 
def add_album_por_genero(albuns: list, genero) -> list:

    """Esta função retorna nossa biblioteca de albuns podendo ser alaterado ou não:
    
    Parâmetros:
        - albuns: nossa biblioteca de albuns

    inputs: 
        - nome do album:
        - nome do artista
        - ano de lançamento do album

    retorna:
        - uma lista com os albuns da nossa biblioteca, com o novo álbum add, caso o mesmo não exista no catálogo
    """
    nome_album = input()
    nome_artista = input()
    ano = int(input())
    albuns.append((nome_album, nome_artista, ano, genero))

    return albuns

albuns_encontrados = buscar_album_por_genero(albuns, genero)

# vamos analisar se existe albuns do gênero procurado

if albuns_encontrados:
    print(f'Nessa galeria há {len(albuns_encontrados)} albuns de {genero}. Os albuns encontrados foram:')
    for album in albuns_encontrados:
        print(f"- {album[0]} do/da artista/banda {album[1]} lançado em {album[2]}")

else:
    print("Você vai precisar adicionar um novo álbum ao catálogo! Não encontramos nenhum álbum desse estilo musical!")
    novo_catalogo = add_album_por_genero(albuns, genero)
    print("Oba, você adicionou um novo estilo musical ao catálogo!")
    print(f"Este foi o novo álbum adcionado:\n- {novo_catalogo[-1][0]} do/da artista/banda {novo_catalogo[-1][1]} lançado em {novo_catalogo[-1][2]}")

 
    

