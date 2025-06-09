def copy_file_content():
    source_file = input("Enter the source file: ")
    destination_file = input("Enter the second file: ")
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)

        print(f"Content has been copied from '{source_file}' to '{destination_file}' successfully!")

    except FileNotFoundError:
        print(f"Error: the file '{source_file}' doesn't exist. Have you typed the name correctly?")

    except Exception as e:
        print(f"An unexpected error has occured: {e}")

if __name__ == "__main__":
    copy_file_content()
