import random
def generar_contraseña():
    nombre = input("Ingresa el Nombre completo: ")
    mayusculas = nombre.upper() #transformo a mayusculas
    minusculas = nombre.lower() #transformo a minusculas
    simbolos = ['!','#','$','&','/','(',')']
    numeros =['1','2','3','4','5','6','7','8','9','0']
    #convierto a listas mis strings
    mayusculas = list(mayusculas)
    minusculas = list(minusculas)
    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []
    for i in range(8):
        caracter_ramdom = random.choice(caracteres)
        contrasena.append(caracter_ramdom)
    contrasena = ''.join(contrasena)
    
    print(contrasena)

def run():
    generar_contraseña()

if __name__ =='__main__':
    run()