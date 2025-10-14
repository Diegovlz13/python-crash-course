
filename = 'pi_digits.txt'

with open(filename) as file_object:
    contenido_archivo = file_object.readlines()
        
for linea in contenido_archivo:
    print(linea.rstrip())