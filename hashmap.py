class MyHashMap:
    """Taula de hash amb UNA SOLA parella per posició (versió de l'escalfament).

    Cada posició de self._table és None o una parella [clau, valor].
    Si dues claus van a la mateixa posició, put() llança KeyError (col·lisió).
    """

    def __init__(self, cap=13):
        self._table = cap * [None]   # m posicions, inicialment buides
        self._n = 0                  # nombre de claus desades

    def _hash_function(self, key):
        return key % len(self._table)          # h(x) = x % m

    def _bucket_put(self, j , key, value):
      if self._table[j] is None:
        self._table[j] = []
      for parella in self._table[j]:
        if parella[0] == key:
          parella[1] = value
          return
      self._table[j].append([key, value])
      self._n += 1

    def _bucket_get(self, j , key):
      if self._table[j] is not None:
        for parella in self._table[j]:
          if parella[0] == key:
            return parella[1]
      return -1

    def _bucket_remove(self, j, key):
      bucket = self._table[j]
      if bucket is None:
        return
      for i in range(len(bucket)):
        if bucket[i][0] == key:
          bucket.pop(i)
          self._n -= 1
          if len(bucket) == 0:
            self._table[j] = None
          return
          
    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        self._bucket_put(j, key, value)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def get(self, key: int) -> int:
        j = self._hash_function(key)
        return self._bucket_get(j, key)

    def remove(self, key: int) -> None:
        j = self._hash_function(key)
        self._bucket_remove(j, key)

    def __len__(self):
        return self._n

    def _resize(self, c):
      copia = self._table
      self._table = c * [None]
      self._n = 0
      for bucket in copia:
        if bucket is not None:
          for key, value in bucket:
            j = self._hash_function(key)
            self._bucket_put(j, key, value)
