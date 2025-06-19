from functions.get_file_content import get_file_content


def test():
    print("Test: main.py")
    print(get_file_content("calculator", "main.py"))
    print("\n")

    print("Test: pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("\n")

    print("Test: /bin/cat")
    print(get_file_content("calculator", "/bin/cat"))
    print("\n")


if __name__ == "__main__":
    test()
