from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
from selenium.common.exceptions import TimeoutException
import FuncoesTeclado as Teclado
from twocaptcha import TwoCaptcha
import os

# --------------------------------------- // ---------------------------------------
#                                    INÍCIO_PROJETO
# --------------------------------------- // ---------------------------------------
#Inicio de abertura de browser CHROME e correção de erros (corrigidos manualmente)

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)
url = 'https://www.portaldoconsignado.com.br/home?0'
navegador = webdriver.Chrome(options=chrome_options)
navegador.get(url)

# --------------------------------------- // ---------------------------------------
# FUNÇÕES

# Função para retornar números randomicos para uso dentro dos sleeps para o sistema reconhecer como retorno organico
def numerosRand():
    randomico = random.randint(3,9)

# --------------------------------------- // ---------------------------------------

sleep(2)
navegador.find_element('xpath', '//*[@id="guias"]/div[2]/span').click()

navegador.find_element('id', 'username').send_keys(Teclado.Keys.BACK_SPACE)
sleep(5)

navegador.find_element('id', 'username').send_keys('Your_User')

navegador.find_element('xpath', '//*[@id="password"]').send_keys('Your_Pass')
sleep(3)

imagem_captcha = navegador.find_element(By.ID, 'cipCaptchaImg')
imagem_captcha.screenshot('captchas/captcha.png')

print("\n")
print("imagens")
print("\n")

chave_api = os.getenv('APIKEY_2CAPTCHA', 'Your_2Captcha_Key_Here')
resolucao = TwoCaptcha(chave_api)

try:
    #print("\n")
    #print("entrou no try")
    #print("\n")
    resultado = resolucao.normal('captchas/captcha.png')

except Exception as e:
    #("\n")
    print("Erro de exceção: " + e)
    #print("\n")

else:
    code = resultado['code']
        
    WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, 'cipCaptchaImg')))    
    navegador.find_element(By.ID, 'captcha').send_keys(code)
    sleep(3)
    navegador.find_element(By.CLASS_NAME, 'botaoAcessar').click()

    sleep(4)

# -------------------- ACIMA, FINAL CAPTCHA -------------------- 

navegador.find_element('xpath', '/html/body/div/div/form/div[2]/div/div[5]/div[2]/fieldset/div/div[1]/span[2]/input').click

navegador.find_element('xpath,' '/html/body/div/div/form/div[2]/div/div[5]/div[2]/fieldset/div/div[2]/fieldset/span/label/input').click()


#navegador.find_element('fullxpath', '')