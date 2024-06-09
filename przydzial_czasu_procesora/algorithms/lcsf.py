def lcsf(processes):
    """
    Funkcja LCSF (Last-Come, First-Served) implementuje algorytm planowania procesów,
    który wykonuje procesy w kolejności odwrotnej do ich przyjścia.

    Parametry:
    - processes: lista słowników reprezentujących procesy, gdzie każdy słownik zawiera klucze 'arrival'
                 (czas przyjścia procesu) i 'burst' (czas wykonywania procesu).

    Zwraca:
    - average_waiting_time: średni czas oczekiwania dla procesów.
    - average_turnaround_time: średni czas cyklu przetwarzania dla procesów.
    - average_response_time: średni czas odpowiedzi dla procesów.
    """
    n = len(processes)
    processes.sort(key=lambda x: x['arrival'], reverse=True)

    waiting_time = 0
    turnaround_time = 0
    response_time = 0
    current_time = 0

    for process in processes:
        arrival_time = process['arrival']
        burst_time = process['burst']

        if current_time < arrival_time:
            current_time = arrival_time

        response_time += current_time - arrival_time
        waiting_time += current_time - arrival_time
        current_time += burst_time
        turnaround_time += current_time - arrival_time

    average_waiting_time = waiting_time / n
    average_turnaround_time = turnaround_time / n
    average_response_time = response_time / n

    return average_waiting_time, average_turnaround_time, average_response_time
