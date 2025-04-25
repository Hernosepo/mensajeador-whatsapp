from src.sesion_whatsapp import SesionWhatsApp

# Ajustá la ruta a tu chromedriver
driver_path = '/ruta/a/tu/chromedriver'

sesion = SesionWhatsApp(driver_path)
sesion.abrir_whatsapp()

if sesion.detectar_sesion_abierta():
    print("Podemos avanzar al siguiente paso.")
else:
    print("Hay que iniciar sesión manualmente.")

sesion.cerrar()