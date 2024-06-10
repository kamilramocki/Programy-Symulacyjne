import random


def lottery(processes):
    """
    Implementacja algorytmu loteryjnego do przydziału czasu procesora.

    Args:
        processes (list): Lista procesów, z których każdy jest reprezentowany jako słownik
                          zawierający 'id' (identyfikator procesu), 'arrival' (czas przybycia procesu)
                          i 'burst' (czas potrzebny do wykonania procesu).

    Returns:
        tuple: Krotka zawierająca średni czas oczekiwania, średni czas cyklu przetwarzania
               i średni czas odpowiedzi.

    Algorithm:
        1. Przydziel każdemu procesowi jeden bilet.
        2. Powtarzaj, dopóki wszystkie procesy nie zostaną wykonane:
            a. Wybierz proces z gotowej kolejki metodą losowania.
            b. Wykonaj proces do zakończenia.
        3. Oblicz średni czas oczekiwania, średni czas cyklu przetwarzania i średni czas odpowiedzi.

    """
    n = len(processes)
    total_tickets = n  # Każdy proces dostaje 1 bilet dla uproszczenia
    tickets = [i for i in range(n)]

    waiting_time = 0
    turnaround_time = 0
    response_time = 0
    current_time = 0
    completed_processes = 0
    first_response = {}

    while completed_processes < n:
        ready_queue = [p for p in processes if p['arrival'] <= current_time and p['burst'] > 0]
        if ready_queue:
            lottery_winner = random.choice(ready_queue)
            process_id = lottery_winner['id']
            arrival_time = lottery_winner['arrival']
            burst_time = lottery_winner['burst']

            if process_id not in first_response:
                first_response[process_id] = current_time - arrival_time
            response_time += first_response[process_id]

            # Załóż, że proces zostanie wykonany do końca
            current_time += burst_time
            waiting_time += current_time - arrival_time - burst_time
            turnaround_time += current_time - arrival_time
            lottery_winner['burst'] = 0  # Proces zostaje ukończony
            completed_processes += 1
            print(waiting_time)
        else:
            current_time += 1

    average_waiting_time = waiting_time / n
    average_turnaround_time = turnaround_time / n
    average_response_time = response_time / n

    return average_waiting_time, average_turnaround_time, average_response_time
