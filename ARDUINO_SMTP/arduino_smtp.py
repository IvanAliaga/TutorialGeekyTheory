'''
   Creada por Ivan Aliaga, el 14 de Octubre del 2013
   Arduino + Python - Envíar un correo electrónico
   Tutorial para http://www.geekytheory.com
'''
# -*- encoding: utf-8 -*-

import serial
import time
import smtplib
 
USUARIO_GMAIL = 'micorreo@gmail.com'
CONTRASENA_GMAIL = 'micontraseña'

DESTINATARIO = 'destinatario@dominio.com'
REMITENTE = 'micorreo@gmail.com'

ASUNTO  = ' ¡ Hay un intruso en su hogar. ! '
MENSAJE = ' ¡ Su sensor de seguridad ha detectado movimiento en su casa. ! '

arduino = serial.Serial('COM4', 9600, timeout = 3.0)    #El puerto se abre inmediatamente en la creación de objetos, cuando se da un puerto.


 
def enviar_correo_electronico():
    print("Envíando e-mail")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)     #Definimos el objeto 'smtpserver' con smptlib.SMTP, SMTP("",) Administra la conexión SMTP
    smtpserver.ehlo()                                   #Este método prepara envíar un correo electrónico
    smtpserver.starttls()                               #Pone la conexión con el servidor SMTP en el modo de TLS.
    smtpserver.ehlo()
    smtpserver.login(USUARIO_GMAIL, CONTRASENA_GMAIL)   #Iniciamos sesion en el SMTP server de Google
    header  = 'To:      ' + DESTINATARIO + '\n'         #Construimos el 'HEADER' para envíar el correo electrónico       
    header += 'From:    ' + REMITENTE    + '\n'
    header += 'Subject: ' + ASUNTO       + '\n'
    print header
    msg = header + '\n' + MENSAJE + ' \n\n'             #Concatenamos el'HEADER' y el 'MENSAJE' del correo electrónico
    smtpserver.sendmail(REMITENTE, DESTINATARIO, msg)   #Envíamos el correo electrónico
    smtpserver.close()                                  #Cerramos la conexión con el SMTP server de Google
    


while True:
    lineaLeida = arduino.readline()                     #Guardo una línea leída desde el puerto serial
    print(lineaLeida)                                   #Imprime la variable mensaje
    if lineaLeida[0] == 'H' :                           #Si la línea contiene a 'H' envía un correo electrónico
        enviar_correo_electronico()                     #Envío un correo electrónico 
    time.sleep(0.5)                                     #Suspende la ejecución por 0.5 segundos   

# EOF
