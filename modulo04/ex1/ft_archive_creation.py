import sys
import typing


def read_archive(file_name: str) -> str | None:
    archive: typing.IO[str] | None = None

    print(f"Accessing file '{file_name}'")

    try:
        archive = open(file_name, "r")
        content = archive.read()
        print("---")
        print(content, end="")
        if content != "" and not content.endswith("\n"):
            print()
        print("---")
        return content
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return None
    finally:
        if archive is not None:
            archive.close()
            print(f"File '{file_name}' closed.")


def transform_data(content: str) -> str:
    lines = content.splitlines()
    transformed = ""

    for line in lines:
        transformed += line + "#\n"

    return transformed


def save_archive(file_name: str, content: str) -> bool:
    archive: typing.IO[str] | None = None

    try:
        archive = open(file_name, "w")
        archive.write(content)
        return True
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return False
    finally:
        if archive is not None:
            archive.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    content = read_archive(sys.argv[1])
    if content is None:
        return

    transformed = transform_data(content)

    print("Transform data:")
    print("---")
    print(transformed, end="")
    print("---")

    new_file = input("Enter new file name (or empty): ")

    if new_file == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")
    if save_archive(new_file, transformed):
        print(f"Data saved in file '{new_file}'.")
    else:
        print("Data not saved.")


if __name__ == "__main__":
    main()
