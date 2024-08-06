import hashlib


class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.count = 0

    def _hash(self, key):
        h = hashlib.shake_256(key.encode("utf-8")).hexdigest(4)
        return int(h, 16) % self.size

    def put(self, key, value):
        # Encrypt the value
        encrypted_value = hashlib.shake_256(str(value).encode("utf-8")).hexdigest(16)
        item = HashItem(key, encrypted_value)
        h = self._hash(key)
        while self.table[h] is not None:
            if self.table[h].key == key:
                break
            h = (h + 1) % self.size
            if self.table[h] is None:
                self.count += 1
        self.table[h] = item

    def get(self, key):
        h = self._hash(key)
        while self.table[h] is not None:
            if self.table[h].key == key:
                return self.table[h].value
            h = (h + 1) % self.size
        return None

    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(
                    f"[{i}] : UserName : {self.table[i].key} PassWord : {self.table[i].value}"
                )
            else:
                print(f"{i} : {self.table[i]}")


h = HashTable(5)

ch = "Y"
# give user input
while ch == "Y" or ch == "y":
    key = input("Enter the UserName : ")
    value = input("Enter the PassWord : ")
    if len(key) == 0 or len(value) == 0:
        print("Please enter valid email and password")
    else:
        h.put(key, value)
        ch = input("Do you want to continue (Y/N) : ")
        ch.upper()
h.display()
