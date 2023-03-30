from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Definindo o caminho para o driver do Chrome
driver_path = 'C:\\Users\\adalb\\Downloads\\chromedriver_win32\\chromedriver.exe'

# determinando o driver do Chrome
driver = webdriver.Chrome(executable_path=driver_path)

# Acessar o site do Medium
driver.get('https://medium.com/')

# Esperar a pagina carregar 
time.sleep(2)

# Rolar a pagina
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# esperando mais um tempo
time.sleep(2)

# Encontrando o primeiro post
post_aleatorio = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[3]/div[1]/div/div/section/div/div/div[1]/div[9]/div/div/div/a')
post_aleatorio.click()


# Esperando a pagina carregar
time.sleep(5)

# Fechando a janela
driver.quit()
