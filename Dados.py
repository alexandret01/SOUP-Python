import pandas as pd
import requests
from bs4 import BeautifulSoup


print('----- Start -----')

reqpt1 = 'https://www.vivareal.com.br/venda/sp/sao-caetano-do-sul/?__vt=srl:a&pagina='
reqpt2 = '#onde=BR-Sao_Paulo-NULL-Sao_Caetano_do_Sul&tipos=apartamento_residencial'

reqpt3 = '#onde=BR-Sao_Paulo-NULL-Sao_Caetano_do_Sul'


for i in range(2, 6):
    req += requests.get(reqpt1+str(i)+reqpt3).content
    print('Pagina: ' + str(i))


content = req


print('----- Soup -----')


soup = BeautifulSoup(content, 'html.parser')

titulos = soup.find_all(class_="property-card__title js-cardLink js-card-title")
enderecos = soup.find_all(class_="property-card__address")
metros_quad = soup.find_all(class_="property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area")
qtd_quartos = soup.find_all(class_="property-card__detail-item property-card__detail-room js-property-detail-rooms")
qtd_banheiros = soup.find_all(class_="property-card__detail-value js-property-card-value")
qtd_vagas = soup.find_all(class_="property-card__detail-value js-property-card-value")
condominios = soup.find_all(class_="js-condo-price")
outros = soup.find_all(class_="property-card__amenities")
precos = soup.find_all(class_="property-card__price js-property-card-prices js-property-card__price-small")



print('----- Prep -----')


for i in range(0, len(outros)):
    if titulos[i] == '':
        titulos[i] = 'Null'
        continue
    if enderecos[i] == '':
        enderecos[i] = 'Null'
        continue
    if precos[i] == '':
        precos[i] = 'Null'
        continue
    if metros_quad[i] == '':
        metros_quad[i] = 'Null'
        continue
    if qtd_quartos[i] == '':
        qtd_quartos[i] = 'Null'
        continue
    if qtd_banheiros[i] == '':
        qtd_banheiros[i] = 'Null'
        continue
    if qtd_vagas[i] == '':
        qtd_vagas[i] = 'Null'
        continue
    if outros[i] == '':
        outros[i] = 'Null'
        continue


print('----- Dict -----')


dados = {}
dados2 = {}
array = []
for i in range(0, len(outros)):
    condominios.append('0')

for i in range(0, len(outros)):
    
     dados[i] = ({
            'id': i,
            'titulo': titulos[i].text,
            'endereco': enderecos[i].text,
            'quartos': qtd_quartos[i].text,
            'banheiros': qtd_banheiros[i].text,
            'vagas': qtd_vagas[i].text,
            'condominio': condominios[i],
            'descricao': outros[i].text,
            'preco': precos[i].text,
            'iptu': '',
    })
    


for i in range(0, len(outros)):
    try:
        dados[i]['condominio'] = dados[i]['condominio'].text
    except:
        continue


print('----- Conversion -----')

df = pd.DataFrame(dados)
df = df.T
df = df.set_index('id')

df.to_csv('dados_scs_AlexandreTambra.csv')

print('----- End -----')


