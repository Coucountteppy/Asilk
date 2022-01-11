#importando librerías
import speech_recognition as sr
import webbrowser
import pywhatkit
import datetime
import os
import random

while True:
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Hola, soy Silk, tu asistente, trata de hablar fuerte y claro, dí 'funciones' para ver las funciones")
    aud = r.listen(source)
    try:
      texto = r.recognize_google(aud)
      #funciones
      print("Haz dicho {}".format(texto))
      
      #imprimir funciones y que hacen
      if "Funciones" in texto:
        print("Contacto: habre el link de mi contacto 'solo dí Contacto' ")
        print("Youtube: abre el video que haz dicho 'solo dí Youtube y el nombre del video' ")
        print("Hora: muestra la fecha y hora actual 'solo dí Hora' ")
        print("Listar: ver tus archivos y directos 'solo dí listar")
        print("Ip: muestra tú IP 'dí cual es mi ip' para mostrarla")
        print("Salir: sales del programa y terminal 'Solo dí Salir' ")
        print("Jugar: te deja elegir un juego 'Solo dí jugar para empezar' ")
        print("Despedida: se despide y da creditos 'Solo dí Despedida' ")
      
      #mi contacto
      if "Contacto" in texto:
        webbrowser.open("http://wa.me/+5076580-9981")
        
      #abriendo y reproduciendo video de youtube
      if "Youtube" in texto:
        pywhatkit.playonyt(texto)
        
      #conversación
      if "hola" in texto:
        print("Hola")
      if "que tal?" in texto:
        print("Todo bien, y usted?")
      if "todo bien" in texto:
        print("Me alegro que este bien, que esta haciendo?")
      if "Adios" in texto:
        print ("Adiós")
       
      #hora/año/día/mes, clima y país
      if "hora" in texto:
        print ("Tú hora es:")
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       
      #ejecutar comandos
      if "listar" in texto:
        os.system("ls")
      if "ip" in texto:
        os.system("curl icanhazip.com")
      if "salir" in texto:
        os.system("exit")
       
      #jugar
      if "Jugar" in texto:
        print("1- numero aleatorio")
        print("2- encuesta")
        juego = int(input("Escribe el numero de tu juego: "))
        if juego == 1:
          numero = random.randint(1, 5)
          tu = int(input("Ingresa tu numero: ")) 
          print ("adivina el numero aleatorio 'solo es del 1-5' ")
          if tu == numero:
            print("Ganaste")
          else:
            print("Perdiste")
          print ("Fin del juego")
            
        if juego == 2:
          pri = input("Cual fue el primer auto de nissan?: ")
          if pri == "Datsun":
            print("Correcto")
          else:
            print("incorreto")
          seg = input("Cuando fue el primer vuelo comercial en México (solo mes)?: ")
          if seg == "Enero":
            print("Correcto")
          else:
            print("Incorrecto")
          ter = input("En que mes salio Minecraft?: ")
          if ter == "Mayo":
            print("Correcto")
          else:
            print("incorreto")
          print ("Fin del juego")
          
       #despedida
       if "despedirse" in texto:
         print ("Adios")
         print("Espero te haya gustado interactuar conmigo")
         print("Mucho gusto de conocerle")
         print ("Proyecto hecho para Valletta")
         print ("Hecho por Coucountteppy/Dezzmain/Sinko")