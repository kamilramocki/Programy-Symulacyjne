import json
from algorithms.lru import LRUCache
from algorithms.lfu import LFUCache
from algorithms.mfu import MFUCache


def load_test_sequences(filename: str):
    """
    Funkcja wczytuje ciągi odwołań stron z pliku JSON.

    Parametry:
    - filename: ciąg znaków reprezentujący nazwę pliku, z którego mają zostać wczytane ciągi odwołań stron.

    Zwraca:
    - Lista zawierająca wczytane ciągi odwołań stron.
    """
    with open(filename, 'r') as f:
        return json.load(f)


def test_algorithm(algorithm_class, R_values, sequences):
    """
    Funkcja przeprowadza testowanie algorytmu wymiany stron na podstawie wczytanych ciągów odwołań stron.

    Parametry:
    - algorithm_class: klasa algorytmu wymiany stron.
    - R_values: lista wartości parametru R do przetestowania dla danego algorytmu.
    - sequences: lista ciągów odwołań stron, na których przeprowadzane będą testy.

    Zwraca:
    - Słownik zawierający średnią liczbę błędów strony dla każdej wartości parametru R.
    """
    results = {R: 0 for R in R_values}

    for R in R_values:
        total_page_faults = 0
        for sequence in sequences:
            cache = algorithm_class(R)
            page_faults = sum(cache.access_page(page) for page in sequence)
            total_page_faults += page_faults
        results[R] = total_page_faults / len(sequences)

    return results


if __name__ == "__main__":
    filename = 'processes.json'

    R_values = [1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 25, 30, 35, 40, 45, 50]

    test_sequences = load_test_sequences(filename)

    # Testowanie algorytmów
    lru_results = test_algorithm(LRUCache, R_values, test_sequences)
    lfu_results = test_algorithm(LFUCache, R_values, test_sequences)
    mfu_results = test_algorithm(MFUCache, R_values, test_sequences)

    print("LRU Results:", lru_results)
    print("LFU Results:", lfu_results)
    print("MFU Results:", mfu_results)
