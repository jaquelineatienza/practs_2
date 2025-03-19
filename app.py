date =  [];

n = int(input('ingrese la cantidad de personas a cargar'))

i = 0
while i < n:
 
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    nota = int(input("Ingresa tu nota: ")) 
    # date.append(nombre,edad,nota)
    newDate = [nombre,edad,nota]
    date.append(newDate)
    i += 1
 


# print(nombre,edad,nota)
datos_ordenados = sorted(date, key=lambda x: x[2], reverse=True)
print(datos_ordenados)
