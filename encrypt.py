import os
import random
import time


def encode(message_file):
    print("Start encrypting ('exit' to exit):")
    message_dict = {}
    combination = []
    combination_cp = []
    try:
        with open(message_file, "w") as file:
            while (text := input("('exit' to exit): ")) != "exit":
                words = text.split()

                for word in words:
                    rand_int = random.randint(1, 1000)
                    while rand_int in message_dict:
                        rand_int = random.randint(1, 1000)

                    message_dict[rand_int] = word

            combination_cp.extend(message_dict)
            combination = combination_cp.copy()
            message_dict = {key: message_dict[key] for key in sorted(message_dict)}

            print()

            print("-" * 10)
            for key in message_dict.keys():
                print(f"{key}: {message_dict[key]}")
                file.write(f"{key}: {message_dict[key]}\n")

            for indx, key in enumerate(message_dict):
                original_index = combination_cp.index(key)
                combination[indx] = original_index

            print(f"\ncombination:{combination}")
            file.write(f"\ncombination:{combination}\n")

            print("-" * 10)
            print()
    except Exception as e:
        print(f"Error at encode: {e}")

    print("Encryption complete. Encrypted words:")


def ensure_txt_extension(filename):
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename


def create_file_if_not_exists(filename):
    if not os.path.exists(filename):
        open(filename, "w").close()
        print(f"File '{filename}' has been created.")
    return filename


def encrypt():
    while (
        filename := input("Enter name of file to encrypt (or 'exit' to exit): ")
    ) != "exit":
        filename = ensure_txt_extension(filename)
        filename = create_file_if_not_exists(filename)
        print()

        try:
            encode(filename)
            print(f"File '{filename}' has been successfully encrypted.")

        except FileNotFoundError:
            print(
                f"Error: The file '{filename}' was not found and could not be encrypted."
            )
        except PermissionError:
            print(f"Error: Permission denied for file '{filename}'.")
        except Exception as e:
            print(f"Error during encryption: {e}")


if __name__ == "__main__":
    print("\n")
    print("Welcome to the encryption program!")
    print("This program will encrypt your input and save it to a file.")
    print("You can also decrypt the file using the decrypt program.")
    print("You can exit the program at any time by typing 'exit'.")
    print("*   © Rhamseys Garcia 2024   *")
    print("-" * 10)
    print()

    messages = [
        "Hacking FBI 0%",
        "Hacking FBI 10%",
        "Hacking FBI 20%",
        "Hacking FBI 30%",
        "Hacking FBI 40%",
        "Hacking FBI 50%",
        "Hacking FBI 60%",
        "Hacking FBI 70%",
        "Hacking FBI 80%",
        "Hacking FBI 90%",
        "Hacking FBI 100",
        "encrypting...",
        "COMPLETE!",
        "Encryption Secure!",
        "Ready!",
    ]

    for message in messages:
        print(message)
        time.sleep(1)

    print()

    encrypt()
