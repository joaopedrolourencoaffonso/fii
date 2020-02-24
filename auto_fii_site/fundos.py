import sys, webbrowser, requests, bs4

string = ""
#file = open("temp.txt", "w")

res = requests.get("https://fiis.com.br/lista-de-fundos-imobiliarios/")
res.raise_for_status()
obj = bs4.BeautifulSoup(res.text, features="html.parser")
objeto = obj.select('.ticker')
#print(objeto)
target = "Cotação atual de"
target1 = "."

for item in objeto:
        txt = str(item)
        temp1 = txt.split('span', 1)
        temp1 = temp1[1].split('>', 1)
        temp1 = temp1[1].split('<', 1)
        res = requests.get("https://fiis.com.br/" + temp1[0] +"/")
        res.raise_for_status()
        obj = bs4.BeautifulSoup(res.text, features="html.parser")
        objeto1 = obj.select("div span")
        tamanho = len(objeto1)
        for i in range(0,tamanho):
                temp4 = str(objeto1[i])
                pos = temp4.find(target)
                if pos > 0:
                        nome = temp1[0]
                        preco = str(objeto1[i-2])
                        preco = preco.split('>')
                        preco = preco[1].split('<')
                        preco = preco[0]

        ###########################################
        objeto1 = obj.select("#informations--indexes")
        objeto1 = str(objeto1)
        objeto1 = objeto1.split("\n")
        temp1 = objeto1[2].split('>')                   ####yield
        temp1 = temp1[1].split('<')
        yield_value = temp1[0]
        #
        temp1 = objeto1[6].split('<')
        temp1 = temp1[3].split('>')             #ultimo rendimento
        ultimo_rend = temp1[1]
        #
        temp1 = objeto1[10].split('<')
        temp1 = temp1[3].split('>')             #patrimonio liquido
        patrimonio = temp1[1]
        #
        temp1 = objeto1[14].split('<')
        temp1 = temp1[3].split('>')             #patrimonio liquido
        valor_patr = temp1[1]
        #
        pos = valor_patr.find(".")

        if pos > 0:
                temp1 = valor_patr.split(".")           #usar prints para descobrir o que está errado
                temp1 = temp1[0] + "" + temp1[1]
                temp1 = temp1.split(",")
                temp1 = temp1[0] + "." + temp1[1]       #calculo de valor float de valor_patr
                temp1 = float(temp1)
        else:
                temp1 = valor_patr.split(",")
                temp1 = temp1[0] + "." + temp1[1]       #calculo de valor float de valor_patr  #dessa maneira funciona
                temp1 = float(temp1)
        #
        pos = preco.find(".")

        if pos > 0:
                temp2 = preco.split(".")
                temp2 = temp2[0] + "" + temp2[1]
                temp2 = temp2.split(",")
                temp2 = temp2[0] + "." + temp2[1]       #calculo de valor float de valor_patr
                temp2 = float(temp2)
        else:
                temp2 = preco.split(",")
                temp2 = temp2[0] + "." + temp2[1]       #calculo de valor float de preco #dessa maneira funciona
                temp2 = float(temp2)
        #
        if temp1 == 0:
                pvp = "0"
        else:
                pvp = temp2 / temp1
                pvp = '%.2f' % pvp
        ##########################################
        site = ' "href=https://fiis.com.br/' + nome + '/" target="_blank"'
        string = string + "<tr> <td> <a" + site + ">" + nome + "</td> <td>" + preco + "</td> <td>" + yield_value + "</td> <td>" + ultimo_rend + "</td> <td>" + patrimonio + "</td> <td>" + valor_patr + "</td> <td>" + pvp + "</td>"


        

string = string + " </tr>"
print(string)
