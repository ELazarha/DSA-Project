import hashlib


class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size  # Initialize the hash table with None
        self.count = 0  # Initialize the count of items in the hash table

    def hashtable(self):
        return self.table

    def _hash(self, key):
        # Generate a hash for the given key using SHAKE-256 and return an integer
        h = hashlib.shake_256(key.encode("utf-8")).hexdigest(4)
        return int(h, 16) % self.size

    def put(self, key, value):
        # Encrypt the value using SHAKE-256
        encrypted_value = hashlib.shake_256(str(value).encode("utf-8")).hexdigest(16)
        item = HashItem(key, encrypted_value)  # Create a new HashItem
        h = self._hash(key)  # Get the hash value for the key
        while self.table[h] is not None:  # Handle collisions using linear probing
            if self.table[h].key == key:  # If the key already exists, break the loop
                break
            h = (h + 1) % self.size  # Move to the next slot
            if self.table[h] is None:  # If an empty slot is found, increment the count
                self.count += 1
        self.table[h] = item  # Insert the item into the hash table

    def get(self, key):
        # Retrieve the value associated with the given key
        h = self._hash(key)  # Get the hash value for the key
        while self.table[h] is not None:  # Search for the key in the hash table
            if self.table[h].key == key:  # If the key is found, return the value
                return self.table[h].value
            h = (h + 1) % self.size  # Move to the next slot
        return None  # Return None if the key is not found

    def display(self):
        # Display the contents of the hash table
        for i in range(self.size):
            if self.table[i] is not None:
                print(
                    f"[{i}] : UserName : {self.table[i].key} PassWord : {self.table[i].value}"
                )
        else:
            # Print None for  all empty slots
            return None

h = HashTable(10)  # Create a hash table of size 5

ch = "Y"
# Loop to get user input
while ch == "Y" or ch == "y":
    key = input("Enter the UserName : ")
    value = input("Enter the PassWord : ")
    if len(key) == 0 or len(value) == 0:
        print("Please enter valid email and password")
    else:
        h.put(key, value)  # Insert the key-value pair into the hash table
        ch = input("Do you want to continue (Y/N) : ")
        ch.upper()
h.display()  # Display the contents of the hash table
