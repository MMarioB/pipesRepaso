import os

'''
padre hijo y nieto: padre manda cosas al hijo y el hijo al nieto
'''
r, w = os.pipe()
r2, w2 = os.pipe()

pid = os.fork()

if pid > 0:
    os.close(r)
    os.close(r2)
    os.close(w2)

    salir = 1
    while (salir != "0"):
        texto = input("\nPADRE: Introduce una frase: ") + "\n"
        text = texto.encode(encoding="utf-8")
        os.write(w, text)
        salir = input("Introduce 0 si quieres salir: ")

    os.close(w)

else:

    pid = os.fork()

    if pid > 0:
        os.close(w)
        os.close(r2)

        r = os.fdopen(r)

        linea = r.readline()
        while (linea):
            os.write(w2, linea.encode(encoding="utf-8"))
            linea = r.readline()

        r.close()
        os.close(w2)

    else:
        os.close(w)
        os.close(r)
        os.close(w2)

        r2 = os.fdopen(r2)
        linea = r2.readline()

        while (linea):
            print("\nNieto: ", linea)
            linea = r2.readline()

        r2.close()
