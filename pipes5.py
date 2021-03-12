import os

'''  
Creamos 2 pipes, dos almacenes para permitir la comunicacion en dos direcciones.
Un pipe se utiliza para que haya comunicacion en un solo sentido, de padre a hijo o de hijo a padre. Se necesitan 2 para que haya en dos sentidos
'''

r1, w1 = os.pipe()
r2, w2 = os.pipe()

print(r1, w1, r2, w2)

pid = os.fork()

# pid greater than 0 represents
# the parent process
if pid > 0:

    # Cerramos los descriptores que no vamos a usar
    os.close(r1)
    os.close(w2)

    # Write some text to file descriptor w
    print("Parent process is writing")
    text = b"cadena1"
    os.write(w1, text)
    text = b"cadena2\n"
    os.write(w1, text)
    text = b"cadena3\n"
    os.write(w1, text)
    os.close(w1)
    r2 = os.fdopen(r2)
    print("Read text:", r2.read())
    # cerramos los descriptores restantes
    r2.close()



else:
    # print(r1,w1,r2,w2)
    # Cerramos los descriptores que no vamos a usar
    os.close(w1)
    os.close(r2)

    # Read the text written by parent process
    print("\nChild Process is reading")
    r1 = os.fdopen(r1)
    print("Read text:", r1.readline())
    print("Read text:", r1.readline())
    r1.close()
    text = b"Mensaje devuelto"
    # w2 = os.fdopen(w2, 'w')
    os.write(w2, text)
    # w2.close()
    # cerramos los descriptores restantes
    os.close(w2)
