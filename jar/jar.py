class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookie = "🍪"
        return cookie * self.size

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("You have depositied too many cookies")
        self.size = self.size + n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Not enought cookies left")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be a positive number")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    print(jar)


if __name__ == "__main__":
    main()
