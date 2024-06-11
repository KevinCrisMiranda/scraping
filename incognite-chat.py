import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configuración para no usar ningún perfil de usuario en Chrome
chrome_options = Options()

# Deshabilitar la carga de imágenes y el uso de la caché
prefs = {"profile.managed_default_content_settings.images": 2, "disk-cache-size": 4096}
chrome_options.add_experimental_option("prefs", prefs)

# Ocultar los encabezados para evitar la detección de Selenium
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Especificar la ubicación del ejecutable de Chrome en Ubuntu
chrome_options.binary_location = '/usr/bin/google-chrome'

# Configuración del servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicialización del WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navegar a la página de Google
driver.get('https://www.google.com')

try:
    time.sleep(5)

    # Obtener el HTML del cuerpo de la página
    body_html = driver.execute_script("return document.body.innerHTML")
    # Analizar el HTML con BeautifulSoup
    soup = BeautifulSoup(body_html, 'html.parser')

    # Suponiendo que 'soup' es tu objeto BeautifulSoup
    inputs = soup.find_all('input')

    # Mostrar los valores de los atributos 'value' de todos los elementos <input>
    for input_tag in inputs:
        if 'value' in input_tag.attrs:
            print("Valor del atributo 'value':", input_tag['value'])

    # Tomar una captura de pantalla de la página
    driver.save_screenshot('google_screenshot.png')

finally:
    # Cerrar el navegador
    driver.quit()