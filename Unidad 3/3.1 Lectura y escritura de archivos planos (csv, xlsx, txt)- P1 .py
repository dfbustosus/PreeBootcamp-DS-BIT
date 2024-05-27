# Abrir el archivo
#ruta="C:/Users/david/Desktop/BIT/Bootcamp-DS-2024-I/Clase 5- 20 Marzo 2024/"
ruta="./"
with open(ruta+'miMascota.txt', 'r',encoding='utf-8') as file:
    # Leer
    contents = file.read()
print(contents)

# Read (No se recomienda hacer)
f=open(ruta+'Data_txt.txt','r',encoding='utf-8')
content=f.read()
print(content)
f.close()

texto= "Hola soy David !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \nCOL vs TYU"

f=open('David_Y.txt','w')
#f.write(d['NOMBRE']+','+d['APELLIDO']+','+str(d['DNI']))
f.write(texto)
f.close()