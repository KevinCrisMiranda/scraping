from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os

# Obtener el nombre de usuario actual
usuario = os.getlogin()

# Configuración para usar el perfil de usuario actual en Chrome
chrome_options = Options()
profile_path = 'C:\\Users\\lexis\\AppData\\Local\\Google\\Chrome\\User Data'
chrome_options.add_argument(f"user-data-dir={profile_path}")
chrome_options.add_argument("profile-directory=Profile 1")

# Especificar la ubicación del ejecutable de Chrome
chrome_options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

# Configuración del servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicialización del WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navegar a la página de Axie Infinity Marketplace
driver.get('https://app.axieinfinity.com/marketplace/axies/?auctionTypes=Sale&parts=ears-nimo&parts=tail-nimo&parts=horn-babylonia&parts=eyes-sleepless&parts=mouth-axie-kiss&parts=back-sandal')

# Esperar un momento para asegurarse de que la página se cargue completamente
import time
time.sleep(5)

# Obtener el HTML del cuerpo de la página
body_html = driver.execute_script("return document.body.innerHTML")

# Analizar el HTML con BeautifulSoup
soup = BeautifulSoup(body_html, 'html.parser')
# Encontrar todos los elementos con la clase especificada para nombres de Axies
names_elements = soup.find_all(class_='text-module_text__ChjB4 text-module_text-2__rIAjt text-module_default__oQBba AxieCard_AxieName__jFA7Z')
# Encontrar todos los elementos con la clase especificada para contenedores de precios de Axies
prices_containers = soup.find_all(class_='CardPrice_Container__aGlzf')

# Obtener el precio de cada Axie
prices = []
for container in prices_containers:
    # Encontrar el div con la clase especificada para el precio dentro del contenedor
    price_element = container.find(class_='CardPrice_FiatPrice__Du6Bm')
    # Extraer el texto del precio y agregarlo a la lista de precios
    if price_element:
        price = price_element.get_text(strip=True)
        prices.append(price)
    else:
        prices.append("Precio no disponible")

# Obtener el texto de cada elemento de nombres y almacenarlo en una lista
names = [element.get_text(strip=True) for element in names_elements]

# Combinar los nombres y precios en una lista
axies_list = [f"{name} - {price}" for name, price in zip(names, prices)]

# Imprimir la lista resultante
print(axies_list)

# Cerrar el navegador
driver.quit()