from bs4 import BeautifulSoup
import requests
import csv
#se extrae informacion de la pagina 
res = requests.get("https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Colombia").text
document=BeautifulSoup(res,"lxml")
tabla1= document.find("table", attrs={"class": "wikitable sortable"})
#sabiendo la estructura del html se extrae la imporcion reelevante en este caso la contenida en la etique tr en elk archivo html.
tabla2=tabla1.find_all("tr")
tabla3=tabla1.find("tbody")
data=[]
table_data = []
headings=[]
for th in tabla2[0].find_all("th"):
    headings.append(th.text.replace("\n"," ").strip())
subtitles=[]
for td in tabla3.find_all("td"):
    subtitles.append(td.text.replace("\n"," ").strip())
listar=[]
for i in range(0, len(subtitles), 5):
    chunk = subtitles[i:i + 5]
    listar.append(chunk)

heading_para_zip=(headings*(len(listar)))
lista_titulos=[]
for g in range(0, len(heading_para_zip), 5):
    titulos = heading_para_zip[i:i + 5]
    lista_titulos.append(titulos)

t_row={}
listaa=[]
for td, th in zip (lista_titulos, listar):
    for tk, tv in zip (td, th):
        t_row[tk] = tv

import pandas as pd
  
# initialize list of lists
data = listar
# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ["Department","Confirmed cases","Confirmed deaths","Recovered","Active cases"])
  
#print(df)
df
df.to_excel(r'Dataframe3.xlsx')