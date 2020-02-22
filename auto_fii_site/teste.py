import sys, webbrowser, requests, bs4

fundos = str(sys.argv[1])
fundos = fundos.split(';')

string = ""

for fii in fundos:
        temp = fii.lower()
        target = "Gerencial"
        res = requests.get("https://fiis.com.br/" + temp + "/")
        res.raise_for_status()
        obj = bs4.BeautifulSoup(res.text, features="html.parser")
        objeto = obj.select('li a')
        lenght = len(objeto)
        #print(lenght)
        i = 0
        #print(objeto)
        while i < lenght:
            info_fii = str(objeto[i])
            i = i + 1
            pos = info_fii.find(target)
            if pos > 0:
                data = info_fii.split('\n', 1)
                site = 'href="' + str(data[0][9:90]) + '/"'
                string = string + '<tr> <td> <a ' + site + ' target="_blank">' +  temp + '</a></td> <td>' + data[1][19:27] + '</td> </tr>'
                #print("Relatório Gerencial: " + data[1][19:27])
                break

print(string)

#print("https://fiis.com.br/" + fii + "/")  

#print("<p>" + fundos[0] + "</p>"
#      + "<br>"
#      + "<p>" + fundos[1] + "</p>")

