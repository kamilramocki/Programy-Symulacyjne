class LRUCache:
    """
    Klasa LRUCache implementuje algorytm Least Recently Used (LRU) dla wymiany stron.
    W tym algorytmie, gdy występuje konflikt o miejsce w pamięci, usuwana jest strona,
    która została najdłużej nieodwołana.

    Parametry:
    - capacity: liczba całkowita określająca maksymalną liczbę stron, jakie mogą być przechowywane
                w pamięci podręcznej.
    """

    def __init__(self, capacity: int):
        """
        Inicjalizuje obiekt klasy LRUCache.

        Parametry:
        - capacity: liczba całkowita określająca maksymalną liczbę stron, jakie mogą być przechowywane
                    w pamięci podręcznej.
        """
        self.cache = {}
        self.capacity = capacity
        self.order = []

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
            self.order.remove(page)
            self.order.append(page)
            return False
        else:
            if len(self.cache) >= self.capacity:
                lru_page = self.order.pop(0)
                del self.cache[lru_page]
            self.cache[page] = True
            self.order.append(page)
            return True
