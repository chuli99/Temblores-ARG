import re 
import bs4 as bs
#from colorama import Fore
from tqdm import tqdm
import pandas as pd
import requests


data = requests.get("https://www.inpres.gob.ar/desktop/")
data = data.text
soup = bs.BeautifulSoup(data, "lxml")


table = soup.find("table", {"id":"sismos","class": "Estilo4"})

print(table)

horas = []
profundidades = []
magnitudes = []
latitudes = []
longitudes = []
provincias = []

for row in tqdm(table.findAll("tr")[1:]):
    hora = row.findAll("td")[2].text
    profundidad = row.findAll("td")[3].text
    magnitud = row.findAll("td")[4].text
    latitud = row.findAll("td")[5].text
    longitud = row.findAll("td")[6].text
    provincia = row.findAll("td")[7].text

    horas.append(hora)
    profundidades.append(profundidad)
    magnitudes.append(magnitud)
    latitudes.append(latitud)
    longitudes.append(longitud)
    provincias.append(provincia)


#Tabla de visualizacion de datos
df = pd.DataFrame(list(zip(horas, profundidades, magnitudes, latitudes, longitudes, provincias)), 
                  columns = ['Hora', 'Profundidad', 'Magnitud', 'Latitud', 'Longitud', 'Provincia'])
df = df.reset_index(drop=True)
print(df)