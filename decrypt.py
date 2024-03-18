def decode(message_file):
    message_dir = {}
    if message_file[-4:] != ".txt":
        message_file += ".txt"
    try:
        with open(message_file) as file_object:
            lines = file_object.readlines()
        for index, line in enumerate(lines):
            try:
                number, message = line.split()
                message_dir[int(number)] = str(message)
            except Exception as e:
                print(f"Syntax error: import .txt file line {index + 1} {e}")
    except Exception as e:
        print(f"Error: Opening the file{message_file} - {e}")

    pyramid_height = 1
    while pyramid_height * (pyramid_height + 1) / 2 <= len(message_dir):
        pyramid_height += 1
    pyramid_height -= 1

    # combination = []

    keys_list = sorted(list(message_dir.keys()))

    def spacing_num(loop):
        # print(f"loop{loop}")
        spacing = 0
        for max_row in range(loop, 1, -1):
            row = pyramid_height - max_row
            for num_idx in range(
                (row * (row + 1)) // 2,
                ((row * (row + 1)) // 2) + row + 2,
            ):
                if num_idx < len(keys_list):
                    spacing += len(str(keys_list[num_idx])) - 1
        spacing = spacing // 4 + loop - 1
        return spacing

    key_index = 0

    for row in range(1, pyramid_height + 1):
        # print(f"pyramid_height{pyramid_height} row{row} key_index{key_index}")
        print(" " * spacing_num(pyramid_height - row + 1), end="")
        for _ in range(row):
            if key_index < len(keys_list):
                print(keys_list[key_index], end=" ")
                key_index += 1
        print()

    sorted_message = [
        message_dir[keys_list[key - 1]]
        for key in [(row * (row + 1)) // 2 for row in range(1, pyramid_height + 1)]
        if key - 1 < len(keys_list) and keys_list[key - 1] in message_dir
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
