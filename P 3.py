def read_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(f"File content:\n{data}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except IOError as e:
        print(f"Error reading the file '{file_path}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_path = "example.txt"

read_data_from_file(file_path)
