import os


def read_as_text(filename: str) -> str:
    with open(filename) as file:
        return file.read()


def read_as_string(filename: str) -> str:
    result = ""
    with open(filename) as file:
        while line := file.readline().rstrip():
            result += line
    return result


def read_as_string_list(filename: str) -> list[str]:
    with open(filename) as file:
        return file.read().splitlines()


def read_as_int(filename: str) -> int:
    with open(filename) as file:
        return int(file.read())

def read_as_int_list(filename: str) -> list[int]:
    with open(filename) as file:
        return list(map(int, file.read().splitlines()))


def file_exists(filepath):
    return os.path.exists(filepath)
