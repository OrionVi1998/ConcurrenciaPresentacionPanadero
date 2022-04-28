import random
import threading
import time

critical_variable = 0


def func_to_run():
    global critical_variable
    thread_id = threading.current_thread().ident

    print(f"{critical_variable}, ID: {thread_id} \n", end="")

    time.sleep(random.randint(0, 2))

    local_read = critical_variable

    time.sleep(random.randint(0, 2))

    local_read += 1

    time.sleep(random.randint(0, 2))

    critical_variable = local_read

    time.sleep(random.randint(0, 2))

    print(f"{critical_variable}, ID: {thread_id} \n", end="")


if __name__ == '__main__':
    t1 = threading.Thread(target=func_to_run)
    t2 = threading.Thread(target=func_to_run)
    t3 = threading.Thread(target=func_to_run)

    t1.start()
    t2.start()
    t3.start()
