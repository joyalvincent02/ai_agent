from functions.run_python_file import run_python_file

def test():
    print("TEST: main.py")
    print(run_python_file("calculator", "main.py"))
    print()

    print("TEST: tests.py")
    print(run_python_file("calculator", "tests.py"))
    print()

    print("TEST: ../main.py")
    print(run_python_file("calculator", "../main.py"))
    print()

    print("TEST: nonexistent.py")
    print(run_python_file("calculator", "nonexistent.py"))
    print()

if __name__ == "__main__":
    test()
