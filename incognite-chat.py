import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configuración para no usar ningún perfil de usuario en Chrome
chrome_options = Options()

# Deshabilitar la carga de imágenes y el uso de la caché
prefs = {"profile.managed_default_content_settings.images": 2, "disk-cache-size": 4096}
chrome_options.add_experimental_option("prefs", prefs)

# Ocultar los encabezados para evitar la detección de Selenium
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Especificar la ubicación del ejecutable de Chrome en Ubuntu
chrome_options.binary_location = '/usr/bin/google-chrome'
# chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# Configuración del servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicialización del WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navegar a la página de Google
driver.get('https://www.google.com')

try:
    # Esperar un momento para que la página se cargue completamente
    time.sleep(5)

    # Ajustar el tamaño de la ventana del navegador para que abarque toda la página
    driver.set_window_size(1920, 1080)  # Tamaño de la ventana (ancho, alto)

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

    # Tomar una captura de pantalla de la página completa
    driver.save_screenshot('google_screenshot.png')

finally:
    # Cerrar el navegador
    driver.quit()