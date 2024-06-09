class LFUCache:
    """
    Klasa LFUCache implementuje algorytm Least Frequently Used (LFU) dla wymiany stron.
    W tym algorytmie, gdy występuje konflikt o miejsce w pamięci, usuwana jest strona,
    która była najrzadziej używana.
    """

    def __init__(self, capacity: int):
        """
        Inicjalizuje obiekt klasy LFUCache.

        Parametry:
        - capacity: liczba całkowita określająca maksymalną liczbę stron, jakie mogą być przechowywane
                    w pamięci podręcznej.
        """
        self.cache = {}
        self.capacity = capacity
        self.freq = {}

    def access_page(self, page: int) -> bool:
        """
        Metoda access_page służy do dostępu do strony w pamięci podręcznej.

        Parametry:
        - page: liczba całkowita reprezentująca numer strony.

        Zwraca:
        - True, jeśli strona była wcześniej w pamięci podręcznej i została odwołana.
        - False, jeśli strona nie była wcześniej w pamięci podręcznej i została dodana.
        """
        if page in self.cache:
            self.freq[page] += 1
            return False
        else:
            if len(self.cache) >= self.capacity:
                lfu_page = min(self.freq, key=self.freq.get)
                del self.cache[lfu_page]
                del self.freq[lfu_page]
            self.cache[page] = True
            self.freq[page] = 1
            return True
