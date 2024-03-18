def decode(message_file):
    message_dir = {}
    if message_file[-4:] != ".txt":
        message_file += ".txt"
    with open(message_file) as file_object:
        lines = file_object.readlines()
    for index, line in enumerate(lines):
        try:
            number, message = line.split()
            message_dir[int(number)] = str(message)

        except Exception as e:
            print(f"Syntax error: import .txt file line {index + 1} {e}")

    pyramid_height = 1
    while pyramid_height * (pyramid_height + 1) / 2 <= len(message_dir):
        pyramid_height += 1
    pyramid_height -= 1

    sorted_numbers = sorted(message_dir)

    for row_indx in range(0, pyramid_height):
        num_in_row = " ".join(
            str(sorted_numbers[(row_indx * (row_indx + 1) // 2) + i])
            for i in range(0, row_indx + 1)
        )
        print(" " * (pyramid_height - row_indx) + num_in_row)

    sorted_message = [
        message_dir[key]
        for key in [(n * (n + 1)) // 2 for n in range(1, pyramid_height + 1)]
        if key in message_dir
    ]
    print(sorted_message)


def decrypt():
    while (
        filename := input("Enter a file name to decrypt (or 'exit' to exit): ")
    ) != "exit":
        try:
            decode(filename)
        except Exception as e:
            print(f"Error decrpt - unexpected: {e}")


if __name__ == "__main__":
    decrypt()
