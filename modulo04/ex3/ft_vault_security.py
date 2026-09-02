def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as archive:
                return (True, archive.read())

        if action == "write":
            with open(file_name, "w") as archive:
                archive.write(content)
            return (True, "Content successfully written to file")

        return (False, f"Unknown action: '{action}'")
    except OSError as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("secured_fragment.txt", "write", result[1]))
    else:
        print((False, "No content available to write"))


if __name__ == "__main__":
    main()
