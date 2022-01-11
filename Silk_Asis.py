#importando librerías
import speech_recognition as sr
import webbrowser
import pywhatkit
import datetime
import os
import random
import pafy

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
        print("Contacto: habre el link de mi contacto")
        print("Youtube: abre el video que haz dicho 'dí Youtube y el nombre del video' ")
        print("Hora: muestra la fecha y hora actual")
        print("Clima: muestra el clima y temperatura actual")
        print("Listar: ver tus archivos y directos")
        print("Ip: muestra tu IP")
        print("Salir: sales del programa")
        print("Jugar: te deja elegir un juego")
        print("Despedida: se despide, da creditos y cierra el programa")
        print("Descargar: descarga audio / video de un video de youtube")
        print ("💢 Para usarlos dí una frase que contenga la palabra de la función o dí solo la función 💢")
      
      #mi contacto
      if "Contacto" in texto:
        webbrowser.open("http://wa.me/+5076580-9981")
        
      #abriendo y reproduciendo video de youtube
      if "Youtube" in texto:
        pywhatkit.playonyt(texto)
      if "Descargar" in texto:
        video = int(input("Quieres descargar video[1] o audio[2]: "))
        if video == 1:
          vid = pafy.new(input("Ingresa el URL de tu video (mp4): "))
          des = vid.getbest(preftype="mp4")
          des.download()
          print("Descarga completa")
        if video == 2:
          aud = pafy.new(input("Ingresa el URL de tu video (mp3): "))
          desaud = aud.getbestaudio()
          desaud.download
          print ("Descarga completa")
          
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
      if "clima" in texto:
        os.system("curl http://v2.wttr.in/")
       
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
        print("3- Cara o Cruz")
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
        if juego == 3:
          lis = ["Cara", "Cruz"]
          ran = random.choice(lis)
          ca = input("Cara o Cruz: ")
          if ran == lis:
            print("correcto")
          else:
            print("incorrecto, la respuesta es ", ran)
       #despedida
       if "despedirse" in texto:
         print ("Adios")
         print("Espero te haya gustado interactuar conmigo")
         print("Mucho gusto de conocerle")
         print ("Proyecto hecho para Valletta")
         print ("Hecho por Coucountteppy/Dezzmain/Sinko")
         os.system ("exit")
    except:
      print("Función no encontrada o no se le ha escuchado")
