#Ten plik zawiera implementację algorytmów FCFS i SJF w wersii wywłaszczeniowej i niewywłaszczeniowej

#funkcje przyjmują listę procesów
#funkcje zwracają średnie czasy oczekiwania procesów

def fcfs (processes):
    time = 0
    queue = []
    sum_wait_time = 0
    l = len(processes)

    while len(processes) > 0 or len(queue) > 0:
        # Pozyskiwanie procesów, które dotarły do bieżącego momentu
        arrived_processes = [p for p in processes if p.arrive_time <= time]     
        arrived_processes.sort(key=lambda p: p.arrive_time)
        queue.extend(arrived_processes)

        # Usuń elementy z listy processes 
        processes = [p for p in processes if p not in arrived_processes]



        if len(queue) > 0:
            current_process = queue.pop(0)

            current_process.wait_time = time - current_process.arrive_time
            sum_wait_time += current_process.wait_time
            # Wykonanie procesu
            for _ in range(current_process.execution_time):
                time+=1


            
        # Brak procesów w kolejce
        elif len(processes) > 0:
            time+=1

    avg = sum_wait_time / l
    return avg

def sjf_non_preemptive (processes):
    time = 0
    queue = []
    sum_wait_time = 0
    l = len(processes)

    while len(processes) > 0 or len(queue) > 0:

        # Pozyskiwanie procesów, które dotarły do bieżącego momentu
        arrived_processes = [p for p in processes if p.arrive_time <= time]     
        queue.extend(arrived_processes)

        # Sortowanie procesy w kolejce według czasu wykonywania
        queue.sort(key=lambda p: p.execution_time)

        # Usuwanie przybyłych procesów z listy processes
        processes = [p for p in processes if p not in arrived_processes]



        if len(queue) > 0:
            current_process = queue.pop(0)

            current_process.wait_time = time - current_process.arrive_time
            sum_wait_time += current_process.wait_time
            # Wykonanie procesu
            for _ in range(current_process.execution_time):
                time+=1


            
        # Brak procesów w kolejce
        elif len(processes) > 0:
            time+=1

    avg = sum_wait_time / l
    return avg

def sjf_preemptive(processes):
    time = 0
    queue = []
    sum_wait_time = 0
    l = len(processes)
    current_process = None

    while len(processes) > 0 or current_process or len(queue) > 0:
        # Pozyskiwanie procesów, które dotarły do bieżącego momentu
        arrived_processes = [p for p in processes if p.arrive_time <= time]
        queue.extend(arrived_processes)

        # Sortowanie procesy w kolejce według czasu wykonywania
        queue.sort(key=lambda p: p.execution_time)

        # Usuwanie przybyłych procesów z listy processes
        processes = [p for p in processes if p not in arrived_processes]

        # Jeśli obecny proces istnieje i przyszedł proces z krótszym czasem wykonania
        if current_process and queue and queue[0].execution_time < current_process.execution_time:
            # Umieszczamy bieżący proces w kolejce
            queue.append(current_process)
            current_process = None

        if not current_process and queue:
            # Jeśli nie ma bieżącego procesu, bierzemy proces z kolejki
            current_process = queue.pop(0)
            current_process.wait_time = time - current_process.arrive_time

        if current_process:

            time += 1
            current_process.execution_time -= 1

            # Jeśli proces zostanie wykonany, ustawiamy jego czas czekania
            if current_process.execution_time == 0:
                time_end = time 

                turn_around_time= time_end - current_process.arrive_time
                current_process.wait_time = turn_around_time - current_process.execution_time_copy
                sum_wait_time += current_process.wait_time
                current_process = None
        else:
            time += 1

    avg = sum_wait_time / l
    return avg
