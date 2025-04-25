# src/sesion_whatsapp.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class SesionWhatsApp:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    def abrir_whatsapp(self):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://web.whatsapp.com/")
        time.sleep(10)  # Esperar tiempo para escanear el QR manualmente

    def detectar_sesion_abierta(self):
        try:
            # Intentamos encontrar el elemento principal de la lista de chats
            self.driver.find_element(By.ID, "pane-side")
            print("✅ Sesión iniciada correctamente.")
            return True
        except:
            print("⚠️ No se detectó sesión iniciada.")
            return False

    def cerrar(self):
        if self.driver:
            self.driver.quit()