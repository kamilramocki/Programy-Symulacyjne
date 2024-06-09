def sjf(processes):
    """
    Implementacja algorytmu Shortest Job First (SJF).

    Parametry:
        processes (list): Lista procesów do przetworzenia. Każdy proces jest słownikiem z kluczami 'id', 'arrival' i 'burst'.

    Zwraca:
        tuple: Krotka zawierająca trzy wartości:
            - Średni czas oczekiwania na przydzielenie procesora.
            - Średni czas cyklu przetwarzania.
            - Średni czas odpowiedzi.
    """
    n = len(processes)
    processes.sort(key=lambda x: (x['arrival'], x['burst']))

    waiting_time = 0
    turnaround_time = 0
    response_time = 0
    current_time = 0
    completed_processes = 0
    ready_queue = []
    first_response = {}

    while completed_processes < n:
        while processes and processes[0]['arrival'] <= current_time:
            ready_queue.append(processes.pop(0))
        if ready_queue:
            ready_queue.sort(key=lambda x: x['burst'])
            process = ready_queue.pop(0)
            arrival_time = process['arrival']
            burst_time = process['burst']
            if process['id'] not in first_response:
                first_response[process['id']] = current_time - arrival_time
            response_time += first_response[process['id']]

            waiting_time += current_time - arrival_time
            current_time += burst_time
            turnaround_time += current_time - arrival_time
            completed_processes += 1
        else:
            current_time += 1

    average_waiting_time = waiting_time / n
    average_turnaround_time = turnaround_time / n
    average_response_time = response_time / n

    return average_waiting_time, average_turnaround_time, average_response_time
