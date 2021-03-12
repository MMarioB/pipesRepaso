import os

r, w = os.pipe()  # padre a hijo2
r2, w2 = os.pipe()  # hijo2 a hijo1
r3, w3 = os.pipe()  # hijo1 a padre

print(r, w, r2, w2, r3, w3)

pid = os.fork()

if pid > 0:
    # PADRE
    pid = os.fork()

    if pid > 0:
        # PADRE
        os.close(r)
        os.close(r2)
        os.close(w2)
        os.close(w3)

        for i in range(1, 11):
            escribir = str(i) + "\n"
            os.write(w, escribir.encode(encoding="utf-8"))
        print("PADRE: ENVIADO A HIJO 2")
        os.close(w)

        r3 = os.fdopen(r3)

        linea = r3.readline()
        while (linea):
            print("PADRE: ", linea)
            linea = r3.readline()
        r3.close()

    else:
        # HIJO2
        os.close(w)
        os.close(r2)
        os.close(r3)
        os.close(w3)

        r = os.fdopen(r)

        linea = r.readline()
        while (linea):
            os.write(w2, linea.encode(encoding="utf-8"))
            linea = r.readline()
        print("HIJO 2: ENVIADO A HIJO 1")
        r.close()
        os.close(w2)

else:
    # HIJO1
    os.close(r)
    os.close(w)
    os.close(w2)
    os.close(r3)

    r2 = os.fdopen(r2)

    linea = r2.readline()
    while (linea):
        os.write(w3, linea.encode(encoding="utf-8"))
        linea = r2.readline()
    print("HIJO 1: ENVIADO A PADRE")
    r2.close()
    os.close(w3)