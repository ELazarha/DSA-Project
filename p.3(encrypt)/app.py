import hashlib


class HashItem:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


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

    def put(self, username, email, password):
        # Encrypt the password using SHAKE-256
        encrypted_password = hashlib.shake_256(password.encode("utf-8")).hexdigest(16)
        item = HashItem(username, email, encrypted_password)  # Create a new HashItem
        h = self._hash(username)  # Get the hash value for the username
        while self.table[h] is not None:  # Handle collisions using linear probing
            if self.table[h].username == username:  # If the username already exists, break the loop
                break
            h = (h + 1) % self.size  # Move to the next slot
            if self.table[h] is None:  # If an empty slot is found, increment the count
                self.count += 1
        self.table[h] = item  # Insert the item into the hash table

    def get(self, username):
        # Retrieve the value associated with the given username
        h = self._hash(username)  # Get the hash value for the username
        while self.table[h] is not None:  # Search for the username in the hash table
            if self.table[h].username == username:  # If the username is found, return the value
                return self.table[h]
            h = (h + 1) % self.size  # Move to the next slot
        return None  # Return None if the username is not found

    def display(self):
        # Display the contents of the hash table
        for i in range(self.size):
            if self.table[i] is not None:
                print(
                    f"[{i}] : UserName : {self.table[i].username}, Email : {self.table[i].email}, "
                    f"Encrypted Password : {self.table[i].password}"
                )
        else:
            # Print None for all empty slots
            return None
    def decrypte(self, password):
        # Decrypt the password using SHAKE-256
        decrypted_password = hashlib.shake_256(password.encode("utf-8")).hexdigest(16)
        return decrypted_password


h = HashTable(10)  # Create a hash table of size 10

while True:
    print("\nMenu:")
    print("1. Add a user")
    print("2. Search for a user")
    print("3. Display all users")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Add a user
        username = str(input("Enter the username: "))
        email = str(input("Enter the email: "))
        password = str(input("Enter the password: "))
        h.put(username, email, password)
    elif choice == "2":
        # Search for a user
        username = str(input("Enter the username to search: "))
        item = h.get(username)
        if item is not None:
            print(
                f"UserName : {item.username}, Email : {item.email}, Encrypted Password : {item.password}"
            )
        else:
            print("User not found")
    elif choice == "3":
        # Display all users
        h.display()
    elif choice == "4":
        # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")