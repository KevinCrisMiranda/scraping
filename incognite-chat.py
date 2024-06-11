from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

# Configuración para no usar ningún perfil de usuario en Chrome
chrome_options = Options()

# Especificar la ubicación del ejecutable de Chrome
chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# Configuración del servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicialización del WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navegar a la página de ChatGPT
driver.get('https://chatgpt.com/')

try:
    # Esperar hasta que el textarea esté presente
    textarea = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'prompt-textarea'))
    )

    # Borrar cualquier texto existente en el textarea
    textarea.clear()

    # Escribir en el textarea
    textarea.send_keys("dame cualquier tipo de preguntas ponlas en una etiqueta <code> q a dentro tenga <uo> y cada una en una <li> solo las preguntas nomas nada mas")

    # Esperar un momento para ver el resultado
    time.sleep(1)

    # Intentar encontrar y hacer clic en el botón con data-testid="fruitjuice-send-button" o data-testid="send-button"
    try:
        send_button = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="fruitjuice-send-button"]'))
        )
        send_button.click()
    except:
        send_button = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="send-button"]'))
        )
        send_button.click()

    # Esperar un momento para ver el resultado después de hacer clic
    time.sleep(30)

finally:
    # Cerrar el navegador
    driver.quit()