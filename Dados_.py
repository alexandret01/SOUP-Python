import pandas as pd
import requests
from bs4 import BeautifulSoup


print('----- Start -----')

reqpt1 = 'https://www.vivareal.com.br/venda/sp/sao-caetano-do-sul/?__vt=srl:a&pagina='
reqpt2 = '#onde=BR-Sao_Paulo-NULL-Sao_Caetano_do_Sul&tipos=apartamento_residencial'

reqpt3 = '#onde=BR-Sao_Paulo-NULL-Sao_Caetano_do_Sul'

y = 0
dados = {}
for i in range(2, 6):
    req = requests.get(reqpt1+str(i)+reqpt2).content
    soup = BeautifulSoup(req, 'html.parser')
    print('Pagina: ' + str(i))
    dados[y] = ({
            'id': y,
            'titulo': (soup.find_all(class_="property-card__title js-cardLink js-card-title"))[y].text,
            'endereco': (soup.find_all(class_="property-card__address")[y]).text,
            'Tamanho m2': soup.find_all(class_="property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area").text,
            'quartos': soup.find_all(class_="property-card__detail-item property-card__detail-room js-property-detail-rooms").text,
            'banheiros': soup.find_all(class_="property-card__detail-value js-property-card-value").text,
            'vagas': soup.find_all(class_="property-card__detail-value js-property-card-value").text,
            'condominio': soup.find_all(class_="js-condo-price").text,
            'descricao': soup.find_all(class_="property-card__amenities").text,
            'preco': soup.find_all(class_="property-card__price js-property-card-prices js-property-card__price-small").text,
            'iptu': '',
    })
    y +=1 

print('----- Conversion -----')

df = pd.DataFrame(dados)
df = df.T
df = df.set_index('id')

df.to_csv('dados_scs_AlexandreTambra.csv')

print('----- End -----')


