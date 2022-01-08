from enum import Enum
import config

class hashset:
    def __init__(self):
        self.verbose = config.verbose
        self.mode = config.mode
        self.hash_table_size = config.init_size
        self.hash_table = [None for i in range(self.hash_table_size)]  # initialise a empty hash table of desired size
        self.insertions = 0  # tracks how many words have been inserted
        self.collisions = 0  # tracks how many collisions have taken place
        self.spelling_errors = 0  # tracks how many spelling mistakes have been identified

    # Helper functions for finding prime numbers
    def isPrime(self, n):
        i = 2
        while (i * i <= n):
            if (n % i == 0):
                return False
            i = i + 1
        return True

    def nextPrime(self, n):
        while (not self.isPrime(n)):
            n = n + 1
        return n

    def hash_function(self, word):  # better hashing function
        ascii_sum = 0
        for char in word:
            ascii_sum += 2**ord(char)
        hash_value = ascii_sum % len(self.hash_table)
        return hash_value

    def linear_probe(self, word):
        hash_value = self.hash_function(word)

        while self.hash_table[hash_value] is not None and self.hash_table[hash_value] != word:
            hash_value = (hash_value + 1) % len(self.hash_table)
            self.collisions += 1
        return hash_value

    def rehash(self):
        hash_value = 0
        temp = self.hash_table  # stores old hash table in temporary array
        self.hash_table = [None for i in range(self.nextPrime(2 * len(temp)))]  # initialize hash_table to 2x size
        for i in range(len(temp)):
            if temp[i] is not None:
                if self.mode == 0 or 4:
                    hash_value = self.linear_probe(temp[i])
                self.hash_table[hash_value] = temp[i]
        return self.hash_table

    def insert(self, word):
        self.insertions += 1
        if self.hash_table[self.linear_probe(word)] != word:  # filters out duplicate inputs
            self.hash_table[self.linear_probe(word)] = word

        if self.insertions / len(self.hash_table) >= 0.75:  # rehash once load factor exceeded
            self.rehash()

    def find(self, word):
        if self.hash_table[self.linear_probe(word)] == word:  # word correctly spelled
            return True

        self.spelling_errors += 1
        return False

    def print_set(self):
        print("\nDictionary output:")
        for i in range(len(self.hash_table)):
            print(i, self.hash_table[i])
        print("\n")

    def print_stats(self):
        if self.insertions == 0:
            print("No insertions were made, mode possibly not implemented")
        else:
            print("Average number of collisions per insertion:", self.collisions / self.insertions)
            print("Misspelled words:", self.spelling_errors)