import json
from algorithms.fcfs import fcfs
from algorithms.lcsf import lcsf
from algorithms.sjf import sjf
from algorithms.lottery import lottery


def test_scheduling_algorithm(algorithm, processes_list):
    """
    Testuje zadany algorytm przydziału czasu procesora na podstawie listy procesów.

    Args:
        algorithm (function): Algorytm do przetestowania.
        processes_list (list): Lista list procesów.

    Returns:
        tuple: Krotka zawierająca średni czas oczekiwania, średni czas cyklu przetwarzania
               i średni czas odpowiedzi.
    """
    avg_waiting_times = []
    avg_turnaround_times = []
    avg_response_times = []

    for processes in processes_list:
        result = algorithm(processes.copy())
        if result is not None:  # Sprawdź, czy algorytm zwrócił poprawne wyniki
            avg_waiting_time, avg_turnaround_time, avg_response_time = result
            avg_waiting_times.append(avg_waiting_time)
            avg_turnaround_times.append(avg_turnaround_time)
            avg_response_times.append(avg_response_time)

    # Sprawdź, czy zostały obliczone wyniki
    if avg_waiting_times:
        overall_avg_waiting_time = sum(avg_waiting_times) / len(processes_list)
        overall_avg_turnaround_time = sum(avg_turnaround_times) / len(processes_list)
        overall_avg_response_time = sum(avg_response_times) / len(processes_list)
        return overall_avg_waiting_time, overall_avg_turnaround_time, overall_avg_response_time
    else:
        return 0, 0, 0  # Zwróć wartości domyślne, jeśli nie wykonano żadnych obliczeń


if __name__ == "__main__":
    with open('one_array_desc.json', 'r') as f:
        processes_list = json.load(f)

    # Testowanie wszystkich algorytmów
    fcfs_results = test_scheduling_algorithm(fcfs, processes_list)
    lcsf_results = test_scheduling_algorithm(lcsf, processes_list)
    sjf_results = test_scheduling_algorithm(sjf, processes_list)
    lottery_results = test_scheduling_algorithm(lottery, processes_list)

    # Wyświetlanie wyników
    print(
        f"FCFS - Średni czas oczekiwania: {fcfs_results[0]:.2f}, Średni czas cyklu przetwarzania: {fcfs_results[1]:.2f}, Średni czas odpowiedzi: {fcfs_results[2]:.2f}")
    print(
        f"LCSF - Średni czas oczekiwania: {lcsf_results[0]:.2f}, Średni czas cyklu przetwarzania: {lcsf_results[1]:.2f}, Średni czas odpowiedzi: {lcsf_results[2]:.2f}")
    print(
        f"SJF - Średni czas oczekiwania: {sjf_results[0]:.2f}, Średni czas cyklu przetwarzania: {sjf_results[1]:.2f}, Średni czas odpowiedzi: {sjf_results[2]:.2f}")
    print(
        f"Lottery - Średni czas oczekiwania: {lottery_results[0]:.2f}, Średni czas cyklu przetwarzania: {lottery_results[1]:.2f}, Średni czas odpowiedzi: {lottery_results[2]:.2f}")
