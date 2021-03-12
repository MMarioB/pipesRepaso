import os

# Padre -> Hijo
PadreHijo_r, PadreHijo_w = os.pipe()

# Hijo -> Nieto
HijoNieto_r, HijoNieto_w = os.pipe()

# Nieto -> Hijo
NietoHijo_r, NietoHijo_w = os.pipe()

# Hijo -> Padre
HijoPadre_r, HijoPadre_w = os.pipe()

pid = os.fork()

if (pid == 0):

    pid = os.fork()
    if (pid == 0):
        print("Soy el nieto", os.getpid(), os.getppid())

        # Cerrar cosas que no se usan
        os.close(PadreHijo_r)
        os.close(PadreHijo_w)

        os.close(HijoNieto_w)

        os.close(NietoHijo_r)

        os.close(HijoPadre_r)
        os.close(HijoPadre_w)

        """------------------------------- LECTURA HIJO -> NIETO ----------------------------"""

        # Abro canal de lectura del Hijo al Nieto
        canal = os.fdopen(HijoNieto_r)

        # Bucle para recibir 10 numeros
        for i in range(10):
            recibido = canal.readline()
            recibido = recibido[:-1]

            print(f"NIETO (mensaje Hijo -> Nieto) = {recibido}")

        # Cierro despues de leer a hijo
        os.close(HijoNieto_r)

        recibido = int(recibido)

        """------------------------------- ESCRITURA NIETO -> HIJO ----------------------------"""

        # Bucle para enviar 10 numeros de nieto a hijo
        for i in range(recibido, recibido + 10):
            num = i + 1
            cadena = str(num) + "\n"
            enviar = cadena.encode("ascii")
            os.write(NietoHijo_w, enviar)

        # Cierro despues de escribir a nieto
        os.close(NietoHijo_w)

    else:
        print("Soy el hijo", os.getpid(), os.getppid())

        # Cerrar cosas que no se usan
        os.close(PadreHijo_w)

        os.close(HijoNieto_r)

        os.close(NietoHijo_w)

        os.close(HijoPadre_r)

        """------------------------------- LECTURA PADRE -> HIJO ----------------------------"""
        # Abro canal de lectura del Padre al Hijo
        canal = os.fdopen(PadreHijo_r)

        # Bucle para recibir 10 numeros
        for i in range(10):
            recibido = canal.readline()
            recibido = recibido[:-1]
            print(f"HIJO (mensaje Padre -> Hijo) = {recibido}")

        # Cierro despues de leer a padre
        os.close(PadreHijo_r)

        recibido = int(recibido)

        """------------------------------- ESCRITURA HIJO -> NIETO ----------------------------"""
        # Bucle para enviar 10 numeros de hijo a nieto
        for i in range(recibido, recibido + 10):
            num = i + 1
            cadena = str(num) + "\n"
            enviar = cadena.encode("ascii")
            os.write(HijoNieto_w, enviar)

        # Cierro despues de escribir a nieto
        os.close(HijoNieto_w)

        """------------------------------- LECTURA NIETO -> HIJO ----------------------------"""
        # Abro canal de lectura del nieto al Hijo
        canal = os.fdopen(NietoHijo_r)

        # Bucle para recibir 10 numeros
        for i in range(10):
            recibido = canal.readline()
            recibido = recibido[:-1]
            print(f"HIJO (mensaje Nieto -> Hijo) = {recibido}")

        # Cierro despues de leer a nieto
        os.close(NietoHijo_r)

        recibido = int(recibido)

        """------------------------------- ESCRITURA HIJO -> PADRE ----------------------------"""

        # Bucle para enviar 10 numeros de hijo a nieto
        for i in range(recibido, recibido + 10):
            num = i + 1
            cadena = str(num) + "\n"
            enviar = cadena.encode("ascii")
            os.write(HijoPadre_w, enviar)

        # Cierro despues de escribir a padre
        os.close(HijoPadre_w)

else:
    print("Padre", os.getpid(), os.getppid())

    # Cerrar cosas que no se usan
    os.close(PadreHijo_r)

    os.close(HijoPadre_w)

    os.close(HijoNieto_r)
    os.close(HijoNieto_w)

    os.close(NietoHijo_r)
    os.close(NietoHijo_w)

    """------------------------------- ESCRITURA PADRE -> HIJO ----------------------------"""

    # Bucle para enviar 10 numeros de padre a hijo
    for i in range(10):
        num = i + 1
        cadena = str(num) + "\n"
        enviar = cadena.encode("ascii")
        os.write(PadreHijo_w, enviar)

    os.close(PadreHijo_w)

    """------------------------------- LECTURA HIJO -> PADRE ----------------------------"""

    # Abro canal de lectura del nieto al Hijo
    canal = os.fdopen(HijoPadre_r)

    # Bucle para recibir 10 numeros
    for i in range(10):
        recibido = canal.readline()
        recibido = recibido[:-1]
        print(f"PADRE (mensaje Hijo -> Padre) = {recibido}")

    # Cierro despues de leer a Hijo
    os.close(HijoPadre_r)