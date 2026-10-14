# Estats d'una posició de la taula (hash tancat). NO canvieu aquests valors.
LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:
    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = [[None, None, LLIURE] for i in range(cap)]   
        self._n = 0                  # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def _find(self, key):
      m = len(self._table)
      j = self._hash_function(key)
      for i in range(m):
        pos = (j + i) % m
        lloc = self._table[pos]
        if lloc[2] == LLIURE:
          return None
        if lloc[2] == OCUPAT and lloc[0] == key:
          return pos
      return None
      
    def put(self, key: int, value: int) -> None:
        pos = self._find(key)
        if pos is not None:
          self._table[pos][1] = value
        else:
          m = len(self._table)
          j = self._hash_function(key)
          for i in range(m):
            p = (j + i) % m
            if self._table[p][2] != OCUPAT:
              self._table[p] = [key, value, OCUPAT]
              self._n += 1
              break
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)  
          
    def get(self, key: int) -> int:
        pos = self._find(key)
        if pos is None:
          return -1
        return self._table[pos][1]

    def remove(self, key: int) -> None:
        pos = self._find(key)
        if pos is not None:
          self._table[pos] = [None, None, ESBORRAT]
          self._n -= 1

    def __len__(self):
        return self._n

    def _resize(self, c):
        old = self._table
        self._table = [[None, None, LLIURE] for _ in range(c)]
        self._n = 0
        for slot in old:
            if slot[2] == OCUPAT:
                self.put(slot[0], slot[1])
