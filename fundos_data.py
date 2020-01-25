import webbrowser, requests, bs4, datetime
from datetime import date, timedelta



#print(vetordata)
#exit()
########

vetor = [0,1,2,3,4,5,6,7]
vetordata = [0,0,0,0,0,0,0,0]
for i in vetor:
    dt = datetime.datetime.now() - timedelta(i)
    datatxt = '{}/{}/{}'.format(dt.day, dt.month, dt.year)
    vetordata[i] = datatxt
    print(vetordata[i])


file = open('C:\\Users\\User\\Desktop\\fii_github\\fundos.txt')
txt = file.readlines()
for i in txt:
        temp = i.split('\n', 1)
        #print("https://fiis.com.br/" + temp[0] + "/")
        target = "Gerencial"
        res = requests.get("https://fiis.com.br/" + temp[0] + "/")
        res.raise_for_status()
        obj = bs4.BeautifulSoup(res.text, features="html.parser")
        objeto = obj.select('a span')
        lenght = len(objeto)
        #print(lenght)
        i = 0
        while i < lenght:
            objeto2 = str(objeto[i])
            i = i + 1
            pos = objeto2.find(target)
            if pos > 0:
                for data in vetordata:
                    pos_data = objeto2.find(data)
                    if pos_data > 1:
                        print(temp[0])
                        print(objeto2)
                #date='30/11/2019'
                #pos1 = objeto2.find(date)
                #print(pos1)
                break



#O caminho do arquivo depende do seu computador, não se esqueça disso
