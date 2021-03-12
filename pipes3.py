import os, random

r_p_h1, w_p_h1 = os.pipe()  # padre a hijo1
r_h1_p, w_h1_p = os.pipe()  # hijo1 a padre
r_p_h2, w_p_h2 = os.pipe()  # padre a hijo2
r_h2_p, w_h2_p = os.pipe()  # hijo2 a padre

print(r_p_h1, w_p_h1, r_h1_p, w_h1_p, r_p_h2, w_p_h2, r_h2_p, w_h2_p)

pid = os.fork()

if pid > 0:
    # PADRE
    pid = os.fork()

    if pid > 0:
        # PADRE
        os.close(r_p_h1)
        os.close(w_h1_p)
        os.close(r_p_h2)
        os.close(w_h2_p)

        r = os.fdopen(r_h1_p)
        r2 = os.fdopen(r_h2_p)

        for i in range(10):
            escribir = str(random.randint(1, 20)) + "\n"
            os.write(w_p_h1, escribir.encode(encoding="utf-8"))
            linea = r.readline()
            print("PADRE: he recibido del hijo 1: " + linea)

            escribir = str(random.randint(1, 20)) + "\n"
            os.write(w_p_h2, escribir.encode(encoding="utf-8"))
            linea2 = r2.readline()
            print("PADRE: he recibido del hijo 2: " + linea2)

        os.close(w_p_h1)
        os.close(w_p_h2)
        r.close()
        r2.close()

    else:
        # HIJO2
        os.close(r_p_h1)
        os.close(w_p_h1)
        os.close(r_h1_p)
        os.close(w_h1_p)
        os.close(w_p_h2)
        os.close(r_h2_p)

        r = os.fdopen(r_p_h2)
        linea = r.readline()

        while (linea):
            print("HIJO 2: he recibido el numero " + linea)
            mult = int(linea) * 3
            escribir = str(mult) + "\n"
            os.write(w_h2_p, escribir.encode(encoding="utf-8"))
            linea = r.readline()

        r.close()
        os.close(w_h2_p)

else:
    # HIJO1
    os.close(r_p_h2)
    os.close(w_p_h2)
    os.close(r_h2_p)
    os.close(w_h2_p)
    os.close(w_p_h1)
    os.close(r_h1_p)

    r = os.fdopen(r_p_h1)

    linea = r.readline()
    while (len(linea) > 1):
        print("HIJO 1: he recibido el numero " + linea)
        mult = int(linea) * 2
        escribir = str(mult) + "\n"
        os.write(w_h1_p, escribir.encode(encoding="utf-8"))
        linea = r.readline()

    r.close()
    os.close(w_h1_p)