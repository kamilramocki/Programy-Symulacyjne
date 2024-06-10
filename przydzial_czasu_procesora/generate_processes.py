import json
import random

def generate_processes(num_sequences=100, num_processes=100):
    """
    Generuje listy procesów i zapisuje je do pliku JSON.

    Parametry:
        num_sequences (int): Liczba ciągów procesów do wygenerowania. Domyślnie 100.
        num_processes (int): Liczba procesów w każdym ciągu. Domyślnie 100.

    Zapisuje:
        Plik 'ascending_processes.json' zawierający wygenerowane ciągi procesów.

    Każdy ciąg procesów jest listą słowników, gdzie każdy słownik reprezentuje pojedynczy proces
    i zawiera klucze 'id', 'arrival' oraz 'burst' odpowiadające identyfikatorowi procesu, czasowi przybycia
    oraz czasowi trwania procesu odpowiednio.

    Przykład użycia:
        generate_processes(num_sequences=50, num_processes=20)

    Generuje 50 ciągów procesów, gdzie każdy ciąg zawiera 20 procesów, a następnie zapisuje je do pliku 'ascending_processes.json'.
    """
    all_sequences = []
    for _ in range(num_sequences):
        processes = []
        base_burst = 1
        for i in range(num_processes):
            #if i % 5 == 0 and i != 0:
            base_burst += 5
            processes.append({
                'id': i,
                'arrival': random.randint(0, 100),
                'burst': base_burst
            })
        all_sequences.append(processes)

    with open('test.json', 'w') as f:
        json.dump(all_sequences, f, indent=4)


if __name__ == "__main__":
    generate_processes(1, 100)
