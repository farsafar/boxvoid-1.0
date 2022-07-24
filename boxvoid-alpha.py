from googlesearch import search
from ytmusicapi import YTMusic
import pywhatkit

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

if anwser() == "/resta":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 - numero2)

if anwser() == "/multiplicacion":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 * numero2)

if anwser() == "/division":
    
    print ("Dime el primer numero")
    numero1 = int(input())
    print ("Dime el segundo numero")
    numero2 = int(input())
    print ("el resultado")
    print (numero1 / numero2)

if anwser() == "/google":
    
    print("Que quieres buscar ")
    busqueda = input()
    pywhatkit.search(busqueda)
        
if anwser() == "/musica":

    print("Que musica quieres escuchar")
    musica = input()
    pywhatkit.playonyt(musica)

if anwser() == "/youtube":

    print("Que Quieres ver")
    videos = input()
    pywhatkit.playonyt(videos)
