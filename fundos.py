import webbrowser, requests, bs4, datetime
from datetime import date, timedelta

vetor_nome = []
vetor_link = []

file = open('C:\\Users\\User\\Desktop\\fii_github\\fundos.txt')
txt = file.readlines()

####################################

k = 0
for fii in txt:
        temp = fii.split('\n', 1)
        target = "Gerencial"
        res = requests.get("https://fiis.com.br/" + temp[0] + "/")
        res.raise_for_status()
        obj = bs4.BeautifulSoup(res.text, features="html.parser")
        objeto = obj.select('li a')
        lenght = len(objeto)
        i = 0
        while i < lenght:
            info_fii = str(objeto[i])
            i = i + 1
            pos = info_fii.find(target)
            if pos > 0:
                print("------------------------")
                print(temp[0])
                data = info_fii.split('\n', 1)
                print("Relatório Gerencial: " + data[1][19:27])
                vetor_nome.insert(k,temp[0])
                vetor_link.insert(k,data[0])
                k = k + 1
                break

####################################
print("Quais você quer ler?")
print("(não esqueça das virgulas)")
escolhidos = input("-->")
abrir = escolhidos.split(',')
for fii in abrir:
    posicao = vetor_nome.index(fii)
    site = vetor_link[posicao][9:90]
    webbrowser.open(site)

    
#Não se esqueça que o caminho do arquivo varia de acordo com seu computador!
