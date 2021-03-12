import os

r, w = os.pipe()

pid = os.fork()

if pid > 0:
    # cierro el de lectura
    os.close(r)

    salir = 1
    texto = ""

    print("Proceso Padre")

    while salir != 0:
        texto = input("\nPADRE: Introduce una frase: ") + "\n"
        text = texto.encode(encoding="utf-8")
        # escribo con la pipe w
        os.write(w, text)

    # cierro la pipe w una vez ya he terminado de escribir
    os.close(w)
    print("Written text:", text.decode())

else:
    # cierro el de escritura
    os.close(w)

    r = os.fdopen(r)
    linea = r.readline()

    while linea:
        print("Linea", linea)
        linea = r.readline()

    # cierro la pipe de lectura
    r.close()
