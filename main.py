print("Hola Mundo") #Imprimir
# python main.py en Consola

#Variables
texto = "Esto es una Variable"
nombre = "José Valduz"
edad = 23
print(f"{texto} - {nombre} - {str(edad)}")
print(texto + "-" + nombre + " - " + str(edad))

#Entrada de datos
sitioweb= input("¿Cual e stu pagina web?:")
print("El sitio web es: " + sitioweb)

#Condiciones
altura = int(input("¿Cual es tu altura?: "))
if  altura >= 180:
    print("Eres una Persona Alta")
else:
    print("Eres bajito")

#funciones
def mostrarAltura():
    altura = int(input("¿Cual es tu altura?: "))
    if  altura >= 180:
        print("Eres una Persona Alta")
    else:
        print("Eres bajito")
    return altura
#llamado a la funcion
resultado= mostrarAltura()
print(resultado)
#LISTAS
personas = ["Victor","Paco","Pepe"]
print(personas)#imprime todo
print(personas[0])#imprime el indicado
#ciclo For
for Persona_n in personas:
    print("-"+Persona_n)
