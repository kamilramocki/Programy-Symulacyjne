import random
import json

def generate_test_sequences(num_sequences: int, sequence_length: int, num_pages: int):
    """
    Funkcja generuje testowe ciągi odwołań stron.

    Parametry:
    - num_sequences: liczba całkowita określająca liczbę ciągów odwołań stron do wygenerowania.
    - sequence_length: liczba całkowita określająca długość każdego ciągu odwołań stron.
    - num_pages: liczba całkowita określająca maksymalny numer strony.

    Zwraca:
    - Lista zawierająca wygenerowane ciągi odwołań stron.
    """
    return [[random.randint(1, num_pages) for _ in range(sequence_length)] for _ in range(num_sequences)]

def save_test_sequences(filename: str, sequences):
    """
    Funkcja zapisuje ciągi odwołań stron do pliku JSON.

    Parametry:
    - filename: ciąg znaków reprezentujący nazwę pliku, do którego mają być zapisane ciągi odwołań stron.
    - sequences: lista zawierająca ciągi odwołań stron do zapisania.
    """
    with open(filename, 'w') as f:
        json.dump(sequences, f)

if __name__ == "__main__":
    num_sequences = 100
    sequence_length = 100
    num_pages = 20
    filename = 'processes.json'

    test_sequences = generate_test_sequences(num_sequences, sequence_length, num_pages)
    save_test_sequences(filename, test_sequences)
