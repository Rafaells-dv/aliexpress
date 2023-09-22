from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import date

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(options=options, service=servico)
navegador.get("https://pt.aliexpress.com/")

item = input()
preco_min = input()
preco_max = input()
navegador.find_element(by=By.ID, value="search-key").send_keys(item, Keys.ENTER)
navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/input[1]').send_keys(preco_min)
navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/input[2]').send_keys(preco_max)
navegador.find_element(By.CLASS_NAME, 'priceInput--ok--2apR64x').click()

lista_elementos = navegador.find_elements(By.CLASS_NAME, 'manhattan--container--1lP57Ag')
produtos = []
for elemento in lista_elementos:
    nome = elemento.find_element(By.CLASS_NAME, 'cards--title--2rMisuY').text
    preco = elemento.find_element(By.CLASS_NAME, 'manhattan--price-sale--1CCSZfK').text
    link = elemento.get_attribute('href')
    produtos.append([nome, preco, link])

tabela_produtos = pd.DataFrame(produtos, columns=['Produto', 'Preço', 'Link'])
hoje = date.today()
tabela_produtos.to_excel('{}.xlsx'.format(hoje))
