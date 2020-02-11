import webbrowser, requests, bs4, datetime
from datetime import date, timedelta

def valor(arg4,arg6,arg7):
        a = int(arg4)
        b = int(arg6)
        c = int(arg7)
        d = a + 0.1*b + 0.01*c
        return d


res = requests.get("https://fiis.com.br/lista-de-fundos-imobiliarios/")
res.raise_for_status()
obj = bs4.BeautifulSoup(res.text, features="html.parser")
objeto = obj.select('.ticker')
target = "Cotação atual de"

for item in objeto:
        txt = str(item)
        temp1 = txt.split('span', 1)
        temp2 = temp1[1].split('>', 1)
        temp3 = temp2[1].split('<', 1)
        res = requests.get("https://fiis.com.br/" + temp3[0] +"/")
        res.raise_for_status()
        obj = bs4.BeautifulSoup(res.text, features="html.parser")
        objeto1 = obj.select("div span")
        tamanho = len(objeto1)
        for i in range(0,tamanho):
                temp4 = str(objeto1[i])
                pos = temp4.find(target)
                if pos > 0:
                        print(temp3[0])
                        print(str(objeto1[i-2]))
                        print("--------")

        objeto1 = obj.select("table")
        target = "R$"
        
        for element in objeto1:
                txt = str(element)
                temp1 = txt.split('td')       
                i = 0
                total = 0
                for line in temp1:
                        pos = line.find(target)
                        if pos > 0:
                                i = i + 1
                                j = i % 2
                                if (j == 0):
                                        numero = valor(line[4], line[6], line[7])
                                        total = total + float(numero)
        print(total)
        break
                
