import re 
import bs4 as bs

from tqdm import tqdm
import pandas as pd
import requests

#Funcion para obtener los datos de la tabla
def service_scrapping():
    data = requests.get("https://www.inpres.gob.ar/desktop/")
    data = data.text
    soup = bs.BeautifulSoup(data, "lxml")


    table = soup.find("table", {"id":"sismos","class": "Estilo4"})

    
    first_row = table.find_all("tr")[1]
    hora = first_row.findAll("td")[2].text
    profundidad = first_row.findAll("td")[3].text
    magnitud = first_row.findAll("td")[4].text
    latitud = first_row.findAll("td")[5].text
    longitud = first_row.findAll("td")[6].text
    provincia = first_row.findAll("td")[7].text
    return(hora, profundidad, magnitud, latitud, longitud, provincia)

#Tabla para visualizacion de datos
def show_table():    
    data = requests.get("https://www.inpres.gob.ar/desktop/")
    data = data.text
    soup = bs.BeautifulSoup(data, "lxml")
    table = soup.find("table", {"id":"sismos","class": "Estilo4"})

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
    
    df = pd.DataFrame(list(zip(horas, profundidades, magnitudes, latitudes, longitudes, provincias)), 
                  columns = ['Hora', 'Profundidad', 'Magnitud', 'Latitud', 'Longitud', 'Provincia'])
    df = df.reset_index(drop=True)
    print(df)
        
