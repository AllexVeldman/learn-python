from pathlib import Path

def using_open():
    """Create or replace a file using the builtin open() function"""
    filename = "hello.txt"
    
    print(f"Creating a file called {filename}")
    with open(filename, mode="w") as file:
        data = input("What would you like to write?: ")
        file.write(data)
    print()

def using_path():
    """Create or replace a file using builtin pathlib.Path"""
    print("Lets create another file")
    filename = input("[filename]: ")

    file = Path(filename)
    data = input("[content]: ")
    file.write_text(data)


if __name__ == "__main__":
    using_open()
    using_path()