from process_generator import generate_processes_normal, generate_processes_uniform, generate_processes_binomial, Process
from cpu_algorithms import fcfs, sjf_non_preemptive, sjf_preemptive
import numpy as np
from page_replacement import Page, fifo, lru, generate_seq_of_pages_binomial


#Ten plik zawiera funkcje testów dla 4 algorytmów



def write_process_data_to_file(processes, title, file_path='process_data.txt'):
    with open(file_path, 'a') as file:
        file.write (f"\n{title}\n")
        for process in processes:
            file.write(f"Process {process.id} - Arrival Time: {process.arrive_time}, "
                       f"Execution Time: {process.execution_time}\n")
        file.write("-----------------------------------------------------------\n")


def write_result_to_file(result, title, file_path='process_data.txt'):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write (f"\n{title}: {result}\n")
        file.write("-----------------------------------------------------------\n")

def test1():
    processes_25 = generate_processes_uniform(25, (1,10), 0)
    write_process_data_to_file(processes_25, "Data for 25 processes")

    processes_75 = generate_processes_uniform(75, (1,10), 0)
    write_process_data_to_file(processes_75, "Data for 75 processes")

    processes_125 = generate_processes_uniform(125, (1,10), 0)
    write_process_data_to_file(processes_125, "Data for 125 processes")



    result_fcfs_25 = fcfs(processes_25)
    result_sjf_NonP_25 = sjf_non_preemptive(processes_25)
    result_sjf_P_25 = sjf_preemptive(processes_25)

    print(f"Średni czas oczekiwania fcfs dla 25 procesów: {result_fcfs_25}")
    print(f"Średni czas oczekiwania sjf_NonP dla 25 procesów: {result_sjf_NonP_25}")
    print(f"Średni czas oczekiwania sjf_P dla 25 procesów: {result_sjf_P_25}")

    write_result_to_file(result_fcfs_25, "Średni czas oczekiwania fcfs dla 25 procesów")
    write_result_to_file(result_sjf_NonP_25, "Średni czas oczekiwania sjf_NonP dla 25 procesów")
    write_result_to_file(result_sjf_P_25, "Średni czas oczekiwania sjf_P dla 25 procesów")




    result_fcfs_75 = fcfs(processes_75)
    result_sjf_NonP_75 = sjf_non_preemptive(processes_75)
    result_sjf_P_75 = sjf_preemptive(processes_75)

    print(f"Średni czas oczekiwania fcfs dla 75 procesów: {result_fcfs_75}")
    print(f"Średni czas oczekiwania sjf_NonP dla 75 procesów: {result_sjf_NonP_75}")
    print(f"Średni czas oczekiwania sjf_P dla 75 procesów: {result_sjf_P_75}")

    write_result_to_file(result_fcfs_75, "Średni czas oczekiwania fcfs dla 75 procesów")
    write_result_to_file(result_sjf_NonP_75, "Średni czas oczekiwania sjf_NonP dla 75 procesów")
    write_result_to_file(result_sjf_P_75, "Średni czas oczekiwania sjf_P dla 75 procesów")







    result_fcfs_125 = fcfs(processes_125)
    result_sjf_NonP_125 = sjf_non_preemptive(processes_125)
    result_sjf_P_125 = sjf_preemptive(processes_125)

    print(f"Średni czas oczekiwania fcfs dla 125 procesów: {result_fcfs_125}")
    print(f"Średni czas oczekiwania sjf_NonP dla 125 procesów: {result_sjf_NonP_125}")
    print(f"Średni czas oczekiwania sjf_P dla 125 procesów: {result_sjf_P_125}")

    write_result_to_file(result_fcfs_125, "Średni czas oczekiwania fcfs dla 125 procesów")
    write_result_to_file(result_sjf_NonP_125, "Średni czas oczekiwania sjf_NonP_ dla 125 procesów")
    write_result_to_file(result_sjf_P_125, "Średni czas oczekiwania sjf_P dla 125 procesów")




def test2():
    processes_25 = generate_processes_binomial(25, 10, (0,10))
    write_process_data_to_file(processes_25, "Data for 25 processes")

    processes_75 = generate_processes_binomial(75, 10, (0,10))
    write_process_data_to_file(processes_75, "Data for 75 processes")

    processes_125 = generate_processes_binomial(125, 10, (0,10))
    write_process_data_to_file(processes_125, "Data for 125 processes")



    result_fcfs_25 = fcfs(processes_25)
    result_sjf_NonP_25 = sjf_non_preemptive(processes_25)
    result_sjf_P_25 = sjf_preemptive(processes_25)

    print(f"Średni czas oczekiwania fcfs dla 25 procesów: {result_fcfs_25}")
    print(f"Średni czas oczekiwania sjf_NonP dla 25 procesów: {result_sjf_NonP_25}")
    print(f"Średni czas oczekiwania sjf_P dla 25 procesów: {result_sjf_P_25}")

    write_result_to_file(result_fcfs_25, "Średni czas oczekiwania fcfs dla 25 procesów")
    write_result_to_file(result_sjf_NonP_25, "Średni czas oczekiwania sjf_NonP dla 25 procesów")
    write_result_to_file(result_sjf_P_25, "Średni czas oczekiwania sjf_P dla 25 procesów")




    result_fcfs_75 = fcfs(processes_75)
    result_sjf_NonP_75 = sjf_non_preemptive(processes_75)
    result_sjf_P_75 = sjf_preemptive(processes_75)

    print(f"Średni czas oczekiwania fcfs dla 75 procesów: {result_fcfs_75}")
    print(f"Średni czas oczekiwania sjf_NonP dla 75 procesów: {result_sjf_NonP_75}")
    print(f"Średni czas oczekiwania sjf_P dla 75 procesów: {result_sjf_P_75}")

    write_result_to_file(result_fcfs_75, "Średni czas oczekiwania fcfs dla 75 procesów")
    write_result_to_file(result_sjf_NonP_75, "Średni czas oczekiwania sjf_NonP dla 75 procesów")
    write_result_to_file(result_sjf_P_75, "Średni czas oczekiwania sjf_P dla 75 procesów")







    result_fcfs_125 = fcfs(processes_125)
    result_sjf_NonP_125 = sjf_non_preemptive(processes_125)
    result_sjf_P_125 = sjf_preemptive(processes_125)

    print(f"Średni czas oczekiwania fcfs dla 125 procesów: {result_fcfs_125}")
    print(f"Średni czas oczekiwania sjf_NonP dla 125 procesów: {result_sjf_NonP_125}")
    print(f"Średni czas oczekiwania sjf_P dla 125 procesów: {result_sjf_P_125}")

    write_result_to_file(result_fcfs_125, "Średni czas oczekiwania fcfs dla 125 procesów")
    write_result_to_file(result_sjf_NonP_125, "Średni czas oczekiwania sjf_NonP_ dla 125 procesów")
    write_result_to_file(result_sjf_P_125, "Średni czas oczekiwania sjf_P dla 125 procesów")







def test3():
    page_seq = np.random.randint(0, 10, 10000)
    frame_size = 3


    result_fifo = fifo(page_seq, frame_size)
    print(f"Liczba czyszczeń ramek fifo: {result_fifo}")

    result_lru = lru(page_seq, frame_size)
    print(f"Liczba czyszczeń ramek lru: {result_lru}")


def test4():
    page_seq = generate_seq_of_pages_binomial(0, 10, 10000)
    frame_size = 7


    result_fifo = fifo(page_seq, frame_size)
    print(f"Liczba czyszczeń ramek fifo: {result_fifo}")

    result_lru = lru(page_seq, frame_size)
    print(f"Liczba czyszczeń ramek lru: {result_lru}")






test1()
test2()
test3()
test4()