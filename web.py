from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Caminho do drive
driver_path = 'C:\\Users\\adalb\\Downloads\\chromedriver_win32\\chromedriver.exe'

# drive do chrome
driver = webdriver.Chrome(executable_path=driver_path)

# Acessar o site
driver.get('https://medium.com/')

# Esperar a pagina carregar 
time.sleep(2)

# Descer a pagina
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# esperando a pagina
time.sleep(2)

# Encontrando post aleatorio
post_aleatorio = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[4]/div[3]/div[1]/div/div/section/div/div/div[1]/div[9]/div/div/div/a')
post_aleatorio.click()


# Esperando a pagina carregar
time.sleep(5)

# Fechando a janela
driver.quit()
