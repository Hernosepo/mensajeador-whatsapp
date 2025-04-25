# 🎯 Automatización de Contacto para Talentos – WhatsApp + Selenium

Este proyecto tiene como objetivo **mejorar la eficiencia en el contacto con talentos para proyectos de casting**, automatizando el envío de mensajes vía WhatsApp Web sin violar sus políticas de uso gratuito.

La solución permite preparar mensajes personalizados y enviarlos uno a uno de manera automatizada, ahorrando tiempo en tareas repetitivas, manteniendo un trato personalizado y sin depender de herramientas de pago.

---

## 🚀 ¿Para qué sirve este sistema?

✅ Enviar mensajes de contacto a talentos para convocatorias, seguimiento o confirmaciones  
✅ Automatizar el proceso sin comprometer la cuenta de WhatsApp  
✅ Usar plantillas personalizables para distintos proyectos  
✅ Registrar errores y resultados de los envíos

---

## ⚙️ ¿Cómo está hecho?

- **Python 3**
- **Selenium WebDriver**
- **Chrome** en modo controlado por script
- **Programación Orientada a Objetos**
- **Sistema de logs para trazabilidad**
- **Entrada por CSV (datos de talentos)**

---

## 📁 Estructura del proyecto

```
mensajeador-whatsapp/
│
├── src/                  → Código fuente (clases: sesión, contacto, mensajeador)
├── data/                 → Archivos CSV con contactos
├── templates/            → Mensajes tipo para distintas convocatorias
├── logs/                 → Registros de actividad
├── README.md             → Este documento
└── requirements.txt      → Dependencias del proyecto
```

---

## 🧩 Desarrollo por etapas

1. **Control de sesión activa en WhatsApp Web**
2. **Carga de datos desde CSV**
3. **Envío de mensajes automatizado**
4. **Validaciones, logs y mejoras para producción**

---

## 👤 Sobre mí

Soy Hernán Geller, administrador general en una agencia de casting en Ciudad de México. Este proyecto nace de una necesidad real: mantener la comunicación con talento de forma ágil y organizada sin depender de soluciones externas costosas.

GitHub: [@Hernosepo](https://github.com/Hernosepo)

---

## ⚠️ Notas importantes

- Este sistema **no viola los términos de uso de WhatsApp**, ya que no envía mensajes masivos ni actúa como spammer.
- Cada mensaje se dispara de forma individual, replicando una interacción humana.