import random
import threading
import time

variable_critica = 0


def func_a_correr(id_hebra):
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


if __name__ == '__main__':
    h1 = threading.Thread(target=func_a_correr, args=[0])
    h2 = threading.Thread(target=func_a_correr, args=[1])
    h3 = threading.Thread(target=func_a_correr, args=[2])

    h1.start()
    h2.start()
    h3.start()
