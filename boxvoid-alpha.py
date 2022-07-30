import pywhatkit
from os import system

#variables

run = ("python3 run.py")

print("Bienvenido a BoxVoid")
print("Cual es tu nombre")
nombre = input ()
print("hola " + nombre)

anwser = input().lower

if anwser() == "/sumar":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 + numero2)
    system(run)

if anwser() == "/resta":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 - numero2)
    system(run)

if anwser() == "/multiplicacion":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 * numero2)
    system(run)

if anwser() == "/division":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 / numero2)
    system(run)

if anwser() == "/google":
    
    print("Que quieres buscar ")
    busqueda = input()
    pywhatkit.search(busqueda)
    system(run)
        
if anwser() == "/musica":

    print("Que musica quieres escuchar")
    musica = input()
    pywhatkit.playonyt(musica)
    system(run)

if anwser() == "/youtube":

    print("Que Quieres ver")
    videos = input()
    pywhatkit.playonyt(videos)
    system(run)

if anwser() == "/update":
    
    update = ("git clone https://github.com/farsafar/boxvoid-alpha ")
    system(update)
    print("elimina esta carpeta y ejecuta la nueva carpeta de boxvoid")
    quit()

if anwser() == "/exit":

    quit()
