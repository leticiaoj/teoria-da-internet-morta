from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import date


class comentar():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def entrar_link(self, link):
        self.driver.get(link)
    

    def pegar_link_das_fotos(self):
        os_links = self.driver.find_elements(By.TAG_NAME, 'a')
        #print(os_links)

        todos_os_links = []
        for os_link in os_links:
            href = os_link.get_attribute("href")
            #print(href)

            if (href.startswith("https://www.instagram.com/katyperry/p/")):
                todos_os_links.append(href)

        return todos_os_links

    def dar_like(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys("l")

        #os_links = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_gA"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div[2]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/div/div').click()

    def comentar(self, comentario):
        textarea = self.driver.find_element(By.TAG_NAME, "textarea")
        time.sleep(1)
        textarea.click()
        time.sleep(1)
        textarea = self.driver.find_element(By.TAG_NAME, "textarea")
        time.sleep(1)
        textarea.clear()
        time.sleep(1)
        textarea.send_keys(comentario)
        time.sleep(2)
        textarea.send_keys(Keys.ENTER)

data_evento = date(2025, 9, 14)
data_atual = date.today()
dias_faltando = (data_evento - data_atual).days
mensagem = f"""Faltam {dias_faltando} dias para o show da Katy Perry!"""

fazer_comentario = comentar()
fazer_comentario.entrar_link("https://www.instagram.com/")
time.sleep(20)
fazer_comentario.entrar_link("https://www.instagram.com/katyperry/")
time.sleep(5)
fazer_comentario.pegar_link_das_fotos()
links_fotos = fazer_comentario.pegar_link_das_fotos()
print(links_fotos)

for link_foto in links_fotos:
    fazer_comentario.entrar_link(link_foto)
    time.sleep(5)
    fazer_comentario.comentar(mensagem)
    time.sleep(100)