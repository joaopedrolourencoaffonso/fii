import webbrowser, requests, bs4, datetime
from datetime import date, timedelta


#vetor_nome = []
#vetor_link = []

#file = open('C:\\Users\\Joaoa\\Desktop\\automação\\fundos.txt')
#txt = file.readlines()

####################################


res = requests.get("https://fiis.com.br/lista-de-fundos-imobiliarios/")
res.raise_for_status()
obj = bs4.BeautifulSoup(res.text, features="html.parser")
objeto = obj.select('.ticker')
#print(objeto)
target = "Cotação atual de"

for item in objeto:
        txt = str(item)
        temp1 = txt.split('span', 1)
        temp2 = temp1[1].split('>', 1)
        temp3 = temp2[1].split('<', 1)
        #print(temp3[0])
        #print("------------")
        res = requests.get("https://fiis.com.br/" + temp3[0] +"/")
        res.raise_for_status()
        obj = bs4.BeautifulSoup(res.text, features="html.parser")
        objeto1 = obj.select("div span")
        tamanho = len(objeto1)
        for i in range(0,tamanho):
                #print(objeto1[i])
                temp4 = str(objeto1[i])
                pos = temp4.find(target)
                if pos > 0:
                        print(temp3[0])
                        print(str(objeto1[i-2]))
                        print("--------")
                

        

#OBS: Esse script ainda não está pronto e como você pode perceber, não é muito eficiente, porém, ele já é capaz de listar todos os preços
#de todos os fundos disponíveis no site fii.com.br, tenho algumas ideias para diminuir o consumo de memória e cálculo de rendimento
#com margem de segurança, mas ainda vai levar um tempinho :)

