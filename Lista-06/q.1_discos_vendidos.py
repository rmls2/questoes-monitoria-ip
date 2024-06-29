
discos_por_artistas = {'Priscila Senna': 40, 'Eduarda': 60, 
                       'Academia da Berlinda': 30, 'Martins': 25, 'Igor de Carvalho': 25}
fortuna_dos_artistas = {'Priscila Senna': 10000, 'Eduarda': 9990, 'Academia da Berlinda': 9995,
                        'Martins': 9970, 'Igor de Carvalho': 9965}
    

# funções para manipulação dos valores dos dicionários 
def lucro_apos_a_tributacao(qtd_discos: int, valor_arrecadado: int) -> float: 
    """ podería ser usado o match case para ficar mais elegante
        porém não sei se essa funcionaldiade é ensinada na cadeira de IP
        ja que é uma estrutura de seleção recente (final de 2021) em python  """ 
    if qtd_discos == 1:
        return valor_arrecadado
    elif qtd_discos > 1 and qtd_discos <= 3:
       return valor_arrecadado*0.98
    elif qtd_discos > 3 and qtd_discos <= 5:
        return valor_arrecadado *0.95
    else:
        return valor_arrecadado*0.93



# input inicial que vai determinar a quantidade de artistas que terão discos vendidos 
numero_de_artistas = int(input(''))
lista_de_artista = []

for i in range(numero_de_artistas):
    artista_selecionado, qtd_discos = input().split(' - ')
    qtd_discos = int(qtd_discos)

    if artista_selecionado in discos_por_artistas.keys():
        
        discos_por_artistas[artista_selecionado] += qtd_discos
        fortuna_dos_artistas[artista_selecionado] += lucro_apos_a_tributacao(qtd_discos, qtd_discos*20) #cada disco custa R$ 20,00
        lista_de_artista.append(artista_selecionado)


print('\nEstes foram os discos vendidos nesta semana:')
for j in lista_de_artista:
    print(f'{j} - Discos vendidos: {discos_por_artistas[j]}')

print('\nEsta é a fortuna atual dos artistas que venderam discos nesta semana:')
for artista, fortuna in fortuna_dos_artistas.items():
    if artista in lista_de_artista:
        print(f'{artista}: R$ {fortuna}')