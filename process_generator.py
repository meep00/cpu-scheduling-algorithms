import numpy as np
import matplotlib.pyplot as plt

#Ten plik zawiera implementację generatora procesów dla algorytmów FIFO i LRU

#funkcje przyjmuję liczbę procesów

#funkcja generate_processes_normal - generuje procesy o czsie wykonania z rozkładu normalnego
#funkcja generate_processes_uniform - generuje procesy o czsie wykonania z rozkładu jednostajnego
#funkcja generate_processes_binomial - generuje procesy o czsie wykonania z rozkładu Bernoulliego

#wszystkie funkcje mogą przyjmować list, tuple lub int jako czas nadejścia procesu


class Process:
    def __init__(self, id, arrive_time, execution_time):
        self.id = id
        self.arrive_time = arrive_time
        self.execution_time = execution_time
        self.execution_time_copy = execution_time # dla sjf_preemptive       
        self.wait_time = 0



#funkcja pomocnicza (podgląd rozkładów)
def show_something(execution_times):
    plt.hist(execution_times, bins=50, color='skyblue', edgecolor='black')
    
    plt.xlabel('Execution Time')
    plt.ylabel('Number of Processes')
    plt.title('Distribution of Execution Time for Randomly Generated Processes')
    plt.grid(True)
    plt.show()



def generate_processes_normal(num_processes, avg_execution_time, std_execution_time, arrival_time):
    #zastosowanie równomiernego rozkładu jest irracjonalne. zadanie wymaga, aby czas wykonania był liczbą całkowitą. rozkład normalny - rozkład ciągły.
    #próba konwersji wygenerowanych wartości float do int wpłynie na kształt rozkłady.
    #lepiej stosować rozkłąd dwumianowy (rozkład Bernoulliego)
    processes = []

    
    if isinstance(arrival_time, (int)):
        arrival_times = [arrival_time] * num_processes
    elif isinstance(arrival_time, (list, tuple)):
        arrival_times = np.random.randint(low= arrival_time[0], high= arrival_time[1], size= num_processes)
    else:
        raise ValueError("arrival_time must be tuple, list or int")

    
    
    execution_times = np.random.normal(loc= avg_execution_time, scale= std_execution_time, size= num_processes).astype(int)
    execution_times = np.clip(execution_times, a_min=0, a_max=None)
    show_something(execution_times)

    for i in range(num_processes):
        processes.append(Process(id=i+1, execution_time=execution_times[i], arrive_time= arrival_times[i]))
    
    return processes



def generate_processes_uniform(num_processes, execution_time_range, arrival_time):
    processes = []

    if isinstance(arrival_time, (int)):
        arrival_times = [arrival_time] * num_processes
    elif isinstance(arrival_time, (list, tuple)):
        arrival_times = np.random.randint(low= arrival_time[0], high= arrival_time[1], size= num_processes)
    else:
        raise ValueError("arrival_time must be tuple, list or int")
    
    
    execution_times = np.random.randint(low= execution_time_range[0], high= execution_time_range[1], size= num_processes)

    
    #show_something(execution_times)

    for i in range(num_processes):
        processes.append(Process(id=i+1, execution_time=execution_times[i], arrive_time= arrival_times[i]))
    
    return processes


def generate_processes_binomial(num_processes, avg_execution_time, arrival_time):
    processes = []


    if isinstance(arrival_time, (int)):
        arrival_times = [arrival_time] * num_processes
    elif isinstance(arrival_time, (list, tuple)):
        arrival_times = np.random.randint(low= arrival_time[0], high= arrival_time[1], size= num_processes)
    else:
        raise ValueError("arrival_time must be tuple, list or int")

    

    p = 0.5  
    n = 2 * avg_execution_time

    execution_times = np.random.binomial(n, p, size=num_processes)

    #show_something(execution_times)

    for i in range(num_processes):
        processes.append(Process(id=i+1, execution_time=execution_times[i], arrive_time=arrival_times[i]))

    
    return processes

