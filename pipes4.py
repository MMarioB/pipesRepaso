import os

'''
Un pipe es un medio de comunicacion enre procesos. Es un almacen temporal de datos en memoria.
Al llamar ala funcion pipe, el sistema operativo crea ese almacen y, a traves de descriptores de fichero, le dice al proceso donde esta el almacen.
Devuelve 2 descriptores ya que por una direccion escribe en el pipe y por la otra lee lo hay en el pipe. Una puerta de entrada y otra diferente de salida
'''
r, w = os.pipe()  # el primero es lectura y el segundo es escritura
# r y w son los descriptores de fichero que le dicen al proceso como escribir y leer en el pipe
print(r, w)

'''
Al duplicar el proceso con fork, los don procesos tienen las direcciones (descriptores de fichero) del almacen por lo que los dos pueden leer y escribir en el mismo almacen.
De esta forma, el almacen se utiliza como medio de comunicacion entre procesos
'''
pid = os.fork()

# pid greater than 0 represents
# the parent process
if pid > 0:

    # Cierra el descriptor r ya que este solo escribe y un descriptor abierto consume memoria
    os.close(r)

    print("Parent process is writing")
    text = b"Hello child process"  # la b delante de la cadena la transforma a bytes
    os.write(w, text)
    print("Written text:", text.decode())


else:

    # # Cierra el descriptor w ya que este proceso solo lee
    os.close(w)

    # Read the text written by parent process
    print("\nChild Process is reading")
    r = os.fdopen(r)  # IMPORTANTE PARA LEER
    leido = r.read()
    print("Read text:", leido, type(leido))