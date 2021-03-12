import os

r, w = os.pipe()
r2, w2 = os.pipe()

pid = os.fork()

if pid > 0:
    os.close(r)
    os.close(w2)
    salir = ""
    texto = ""
    while (salir != "0"):
        texto = input("\nPADRE: Introduce una frase: ") + "\n"
        text = texto.encode(encoding="utf-8")
        os.write(w, text)
        salir = input("Introduce 0 si quieres salir: ")

    os.close(w)

    r2 = os.fdopen(r2)
    linea = r2.readline()

    while (linea):
        print("Padre: ", linea)
        linea = r2.readline()

    r2.close()

else:
    os.close(w)
    os.close(r2)

    r = os.fdopen(r)
    linea = r.readline()

    while (linea):
        print("Hijo: ", linea)
        linea = r.readline()

    r.close()

    salir = "1"
    texto = ""
    while salir == "1":
        texto = input("\nPADRE: Introduce una frase: ") + "\n"
        text = texto.encode(encoding="utf-8")
        os.write(w2, text)
        salir = input("Introduce 0 si quieres salir: ")

    os.close(w2)
