import numpy as np
from cryptography.fernet import Fernet
import os


# Function to generate a key if it doesn't exist
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Function to load the key from file or generate if not exist
def load_key():
    if not os.path.exists("key.key"):
        generate_key()
    with open("key.key", "rb") as file:
        key = file.read()
    return key


# Load the key
key = load_key()
fer = Fernet(key)  # Instantiate Fernet with the loaded key


# Function to view passwords
def view():
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No passwords stored yet.")
                return
            for line in lines:
                data = line.rstrip()
                if "|" not in data:
                    print("Invalid format in passwords file:", data)
                    continue  # Skip to the next line
                user, passw = data.split("|")
                try:
                    decrypted_pass = fer.decrypt(passw.encode()).decode()
                    print("user:", user, "| password:", decrypted_pass)
                except Exception as e:
                    print("Error decrypting password:", e)
    except FileNotFoundError:
        print("Password file not found. Creating a new one.")
        with open("passwords.txt", "w") as f:
            pass  # Just creating the file


# Function to add passwords
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + encrypted_pwd + "\n")


# Main loop
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add) Press 'q' to quit: "
    ).lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")

    """def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
    """
