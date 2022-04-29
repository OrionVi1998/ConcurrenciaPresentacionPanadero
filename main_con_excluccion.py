import random
import threading
import time

variable_critica = 0
entrando = [False, False, False]
numero_de_turno = [0, 0, 0]


def protocolo_de_entrada(id_hebra):
    entrando[id_hebra] = True
    numero_de_turno[id_hebra] = 1 + max(numero_de_turno)
    entrando[id_hebra] = False

    for j in range(len(entrando)):
        while entrando[j]:
            pass
        while numero_de_turno[j] != 0 and (numero_de_turno[j] < numero_de_turno[id_hebra] or (
                numero_de_turno[j] == numero_de_turno[id_hebra] and j < id_hebra)):
            pass


def sec_critica(id_hebra):
    global variable_critica

    print(f"ID: {id_hebra} | START | Variable Critica: {variable_critica} \n", end="")
    time.sleep(random.randint(0, 2))

    variable_local = variable_critica
    time.sleep(random.randint(0, 2))

    variable_local += 1
    time.sleep(random.randint(0, 2))

    variable_critica = variable_local
    time.sleep(random.randint(0, 2))

    print(f"ID: {id_hebra} | END | Variable Critica: {variable_critica} \n", end="")


def protocolo_de_sailda(id_hebra):
    numero_de_turno[id_hebra] = 0


def funcion_a_correr(id_hebra):
    protocolo_de_entrada(id_hebra)
    sec_critica(id_hebra)
    protocolo_de_sailda(id_hebra)


if __name__ == '__main__':
    h1 = threading.Thread(target=funcion_a_correr, args=[0])
    h2 = threading.Thread(target=funcion_a_correr, args=[1])
    h3 = threading.Thread(target=funcion_a_correr, args=[2])

    h1.start()
    h2.start()
    h3.start()
