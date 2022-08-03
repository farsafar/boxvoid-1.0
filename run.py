import pywhatkit
from os import system

run = ("python3 run.py")
alpha = ("python3 alpha.py")

anwser = input("/").lower

if anwser() == "/sumar":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 + numero2)
    system("run")

if anwser() == "/resta":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 - numero2)
    system("run")

if anwser() == "/multiplicacion":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 * numero2)
    system("run")

if anwser() == "/division":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 / numero2)
    system("run")

if anwser() == "/google":
    
    print("Que quieres buscar ")
    busqueda = input()
    pywhatkit.search(busqueda)
    system("run")
        
if anwser() == "/musica":

    print("Que musica quieres escuchar")
    musica = input()
    pywhatkit.playonyt(musica)
    system("run")

if anwser() == "/youtube":

    print("Que Quieres ver")
    videos = input()
    pywhatkit.playonyt(videos)
    system("run")

if anwser() == "/update":
    
    update = ("git clone https://github.com/farsafar/boxvoid-1.0") 
    system(update)
    print("metete a la carpeta boxvoid-alpha y dentro de esa carpeta habra otra carpeta con el mismo nombre mueva esa carpeta y elimine la antigua carpeta")
    quit()

if anwser() == "/cmd":
    cmd = input("$ ")
    system(cmd)
    system(run)

if anwser() == "/exit":
    
    quit()

if anwser() == "alpha":

    print("ejecutando nuevo codigo...")
    print("ejecutando nuevo codigo...")
    system("clear")
    system(alpha)
