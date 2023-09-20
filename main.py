from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(options=options, service=servico)
navegador.get("https://pt.aliexpress.com/")

item = input()
pesquisar = navegador.find_element(by=By.ID, value="search-key").send_keys(item, Keys.ENTER)
