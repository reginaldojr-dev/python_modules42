import sys
import typing


def recover_file(file_name: str) -> None:
    archive: typing.IO[str] | None = None

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        archive = open(file_name, "r")
        content = archive.read()
        print("---")
        print(content, end="")
        if content != "" and not content.endswith("\n"):
            print()
        print("---")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
    finally:
        if archive is not None:
            archive.close()
            print(f"File '{file_name}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    recover_file(sys.argv[1])


if __name__ == "__main__":
    main()
