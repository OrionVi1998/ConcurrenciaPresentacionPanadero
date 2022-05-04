import threading
import random
import time

variable_critica = 0
entrando = [False, False, False]
numero_de_turno = [0, 0, 0]


def protocolo_de_entrada(id_hebra):
    # Proceso entrando
    entrando[id_hebra] = True
    # Calcula el numero del turno
    numero_de_turno[id_hebra] = 1 + max(numero_de_turno)
    # Proceso consiguió turno
    entrando[id_hebra] = False

    # Por cada proceso
    for j in range(len(entrando)):
        # Si el proceso j está entrando
        while entrando[j]:
            pass

        # Si el proceso j tiene un número de turno Y
        # el número del proceso j es menor al número de turno de este proceso
        while numero_de_turno[j] != 0 and (numero_de_turno[j] < numero_de_turno[id_hebra] or (

                # Si el número de turno del proceso j es igual al número de turno de este proceso
                # Y el proceso j tiene ID menor al ID de este programa
                numero_de_turno[j] == numero_de_turno[id_hebra] and j < id_hebra)):
            pass


def sec_critica():
    global variable_critica

    time.sleep(random.randint(0, 2))

    # LEER
    variable_local = variable_critica
    time.sleep(random.randint(0, 2))

    # INCREMENTAR
    variable_local += 1
    time.sleep(random.randint(0, 2))

    # GUARDAR
    variable_critica = variable_local
    time.sleep(random.randint(0, 2))


def protocolo_de_salida(id_hebra):
    # El numero de turno del proceso vuelve a 0
    numero_de_turno[id_hebra] = 0


def func_a_correr(id_hebra):
    print(f"ID: {id_hebra} | START | Variable Critica: {variable_critica} \n", end="")
    time.sleep(random.randint(0, 2))

    protocolo_de_entrada(id_hebra)
    sec_critica()
    protocolo_de_salida(id_hebra)

    print(f"ID: {id_hebra} | END | Variable Critica: {variable_critica} \n", end="")


if __name__ == '__main__':
    h1 = threading.Thread(target=func_a_correr, args=[0])
    h2 = threading.Thread(target=func_a_correr, args=[1])
    h3 = threading.Thread(target=func_a_correr, args=[2])

    h1.start()
    h2.start()
    h3.start()
