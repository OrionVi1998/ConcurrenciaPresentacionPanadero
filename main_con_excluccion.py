import random
import threading
import time

critical_variable = 0
entering = [False, False, False]
turn_number = [0, 0, 0]


def entrance_protocol(thread_id):
    entering[thread_id] = True
    turn_number[thread_id] = 1 + max(turn_number)
    entering[thread_id] = False

    for j in range(len(entering)):
        while entering[j]:
            pass
        while turn_number[j] != 0 and (turn_number[j] < turn_number[thread_id] or (
                turn_number[j] == turn_number[thread_id] and j < thread_id)):
            pass


def critical_section(thread_id):
    global critical_variable

    print(f"{critical_variable}, ID: {thread_id} \n", end="")

    time.sleep(random.randint(0, 2))

    local_read = critical_variable

    time.sleep(random.randint(0, 2))

    local_read += 1

    time.sleep(random.randint(0, 2))

    critical_variable = local_read

    time.sleep(random.randint(0, 2))

    print(f"{critical_variable}, ID: {thread_id} \n", end="")


def exit_protocol(thread_id):
    turn_number[thread_id] = 0


def func_to_run(thread_id):
    entrance_protocol(thread_id)
    critical_section(thread_id)
    exit_protocol(thread_id)


if __name__ == '__main__':
    t1 = threading.Thread(target=func_to_run, args=[0])
    t2 = threading.Thread(target=func_to_run, args=[1])
    t3 = threading.Thread(target=func_to_run, args=[2])

    t1.start()
    t2.start()
    t3.start()
