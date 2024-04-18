### PARTE 1 ###


discos_por_artistas = {'Priscila Senna': 40, 'Eduarda': 60, 
                       'Academia da Berlinda': 30, 'Martins': 25, 'Igor de Carvalho': 25}
fortuna_dos_artistas = {'Priscila Senna': 10000, 'Eduarda': 9990, 'Academia da Berlinda': 9995,
                        'Martins': 9970, 'Igor de Carvalho': 9965}

# podería ser usado o match case para ficar mais elegante
# porém não sei se essa funcionaldiade é ensinada na cadeira de IP 

def lucro_apos_a_tributacao(qtd_discos, valor_arrecadado):  
    if qtd_discos == 1:
        return valor_arrecadado
    elif qtd_discos > 1 and qtd_discos <= 3:
       return valor_arrecadado*0.98
    elif qtd_discos > 3 and qtd_discos <= 5:
        return valor_arrecadado *0.95
    else:
        return valor_arrecadado*0.93
  
# input inicial que vai determinar a quantidade de artistas 
# cujos albuns serão adquiridos 
numero_de_artistas = int(input('Digite o número de artistas selecionados: '))

for i in range(numero_de_artistas):
    artista_selecionado, qtd_discos = input().split(' - ')
    qtd_discos = int(qtd_discos)

    if artista_selecionado in discos_por_artistas.keys():
        
        discos_por_artistas[artista_selecionado] += qtd_discos
        fortuna_dos_artistas[artista_selecionado] += lucro_apos_a_tributacao(qtd_discos, qtd_discos*20) #cada disco custa R$ 20,00

# print para ver as modificaçõs feitas até o momento e se o código reage como esperado
print(discos_por_artistas)
print(fortuna_dos_artistas)