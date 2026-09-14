def copy_file(command: str) -> None:
    if len(command) > 0:
        command_to_list = command.split(" ")
        if len(command_to_list) == 3:
            needed_command = command_to_list[0]
            file_name = command_to_list[1]
            new_file_name = command_to_list[2]
            if needed_command == "cp" and file_name != new_file_name:
                try:
                    with open(file_name, "r") as file_in:
                        with open(new_file_name, "w") as file_out:
                            data = file_in.read()
                            file_out.write(data)
                except FileNotFoundError:
                    pass
