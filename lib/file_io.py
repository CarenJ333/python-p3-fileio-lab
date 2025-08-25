def write_file(file_name, file_content):
    full_file_name = f"{file_name}.txt"

    with open(full_file_name, "w", encoding="utf-8") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    full_file_name = f"{file_name}.txt"

    with open(full_file_name, mode="a", encoding="utf-8") as f:
        f.write(append_content)

def read_file(file_name):
    full_file_name = f"{file_name}.txt"

    with open(full_file_name, mode="r", encoding="utf-8") as f:
        return f.read()
