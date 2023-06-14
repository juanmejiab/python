from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mensaje = MIMEMultipart()
mensaje["from"] = "Remitente"
mensaje["to"] = "correo@gmail.com"
mensaje["subject"] = "Mensaje de prueba"
mensaje.attach(MIMEText("Cuerpo del mensaje"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("correo@gmail.com", "contrasena")
    smtp.send_message(mensaje)
    print("Mensaje enviado.")
