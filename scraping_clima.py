#Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

#Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

url="https://www.clima.com"
driver.get(url)

#Selecciona el pais PERU
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'li.m_list_countrys_pe')))\
.click()

#Ingresa en la caja de texto Lima
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'input#inputSearch')))\
.send_keys('Lima')

#Click en el icono Buscar
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'i.icon.icon-search')))\
.click()

#Selecciona la primera opcion Lima, Lima
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'i.icon_weather_s.icon.icon-local')))\
.click()

#Selecciona la pestaña "Por horas"
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="cityTable"]/div/article/section/ul/li[2]/a')))\
.click()

#La informacion del día de hoy
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="main"]/div[4]/div/section[3]/section/div[1]/ul/li[1]')))

#Guarda en una variable
info_columnas = driver.find_elements_by_xpath('//*[@id="main"]/div[4]/div/section[3]/section/div[1]/ul/li[1]')
info_columnas = info_columnas[0].text
#print(info_columnas)

horas = list()
tempe = list()
velo = list()

clima_hoy = info_columnas.split("\n")
clima_hoy.remove("Hoy")

for i in range(0,len(clima_hoy),4):
    horas.append(clima_hoy[i])
    tempe.append(clima_hoy[i+1])
    velo.append(clima_hoy[i+2])

#Crea un dataframe
df = pd.DataFrame({"Hora":horas, "Temperatura":tempe, "Vel_Viento(km/h)":velo})
print(df)

#Guarda en un archivo csv
df.to_csv('clima_hoy.csv', index=False)

time.sleep(2)

driver.quit()