import os

r, w = os.pipe()  # padre a hijo
r2, w2 = os.pipe()  # hijo a nieto
r3, w3 = os.pipe()  # nieto a hijo
r4, w4 = os.pipe()  # hijo a padre

print(r, w, r2, w2, r3, w3, r4, w4)
pid = os.fork()

if pid > 0:
    os.close(r)
    os.close(r2)
    os.close(w2)
    os.close(r3)
    os.close(w3)
    os.close(w4)

    # escribe para enviarselo al hijo y que este se lo envie al nieto
    salir = ""
    while (salir != "0"):
        texto = input("\nPADRE: Introduce una frase: ") + "\n"
        text = texto.encode(encoding="utf-8")
        os.write(w, text)
        salir = input("Introduce 0 si quieres salir: ")

    os.close(w)

    r4 = os.fdopen(r4)

    # lee lo que ha escrito el nieto
    linea = r4.readline()
    while (linea):
        print("\nPadre: ", linea)
        linea = r4.readline()

    r4.close()

else:

    pid = os.fork()

    if pid > 0:
        os.close(w)
        os.close(r2)
        os.close(w3)
        os.close(r4)

        # lee lo que ha escrito el padre y se lo envia al nieto
        r = os.fdopen(r)

        linea = r.readline()
        while (linea):
            os.write(w2, linea.encode(encoding="utf-8"))
            linea = r.readline()

        r.close()
        os.close(w2)

        # Lee lo que ha escrito el nieto y lo escribe para que lo lea el padre
        r3 = os.fdopen(r3)

        linea = r3.readline()
        while (linea):
            os.write(w4, linea.encode(encoding="utf-8"))
            linea = r3.readline()

        r3.close()
        os.close(w4)

    else:
        os.close(w)
        os.close(r)
        os.close(w2)
        os.close(r3)
        os.close(r4)
        os.close(w4)

        # lee lo que le ha enviado el hijo que ha escrito el padre
        r2 = os.fdopen(r2)

        linea = r2.readline()
        while (linea):
            print("\nNieto: ", linea)
            linea = r2.readline()

        r2.close()

        # escribe para enviarselo al hijo y que este lo envie al padre
        salir = ""
        while (salir != "0"):
            texto = input("\nNIETO: Introduce una frase: ") + "\n"
            text = texto.encode(encoding="utf-8")
            os.write(w3, text)
            salir = input("Introduce 0 si quieres salir: ")
        os.close(w3)