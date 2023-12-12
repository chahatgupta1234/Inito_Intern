# filesystem.py
class FileSystem:
    def __init__(self):
        # Initialize your in-memory file system structure here
        self.current_directory = {'/': {}}
        self.current_path = '/'

    def mkdir(self, directory_name):
        # Create a new directory
        new_path = f"{self.current_path}/{directory_name}"
        self.current_directory[new_path] = {}
        print(f"Directory '{directory_name}' created at {new_path}")

    def cd(self, directory_path):
        # Change the current directory
        if directory_path == '..':
            # Move to the parent directory
            self.current_path = '/'.join(self.current_path.split('/')[:-1])
        elif directory_path.startswith('/'):
            # Move to an absolute path
            self.current_path = directory_path
        else:
            # Move to a relative path
            self.current_path = f"{self.current_path}/{directory_path}"

        print(f"Current directory: {self.current_path}")

    def ls(self, directory_path=""):
        # List contents of the specified directory
        target_path = directory_path if directory_path else self.current_path
        contents = self.current_directory.get(target_path, {})
        print(f"Contents of {target_path}: {list(contents.keys())}")

    def touch(self, file_name):
        # Create a new empty file
        file_path = f"{self.current_path}/{file_name}"
        self.current_directory[file_path] = ""
        print(f"File '{file_name}' created at {file_path}")

    def save_state(self, file_path):
        # Save the current state to a file
        with open(file_path, 'w') as file:
            file.write(str(self.current_directory))
        print(f"File system state saved to {file_path}")

    def load_state(self, file_path):
        # Load the state from a file
        with open(file_path, 'r') as file:
            content = file.read()
            self.current_directory = eval(content)
        print(f"File system state loaded from {file_path}")

if __name__ == "__main__":
    filesystem = FileSystem()

    while True:
        command = input("Enter command: ")

        # Implement command parsing and execution here
        tokens = command.split()
        operation = tokens[0]

        if operation == 'mkdir':
            if len(tokens) > 1:
                filesystem.mkdir(tokens[1])
                break  # Exit the loop after executing mkdir
            else:
                print("Error: Missing directory name for mkdir command.")
        elif operation == 'cd':
            if len(tokens) > 1:
                filesystem.cd(tokens[1])
            else:
                print("Error: Missing directory path for cd command.")
        elif operation == 'ls':
            filesystem.ls(tokens[1] if len(tokens) > 1 else "")
        elif operation == 'touch':
            if len(tokens) > 1:
                filesystem.touch(tokens[1])
            else:
                print("Error: Missing file name for touch command.")
        elif operation == 'save_state':
            if len(tokens) > 1:
                filesystem.save_state(tokens[1])
            else:
                print("Error: Missing file path for save_state command.")
        elif operation == 'load_state':
            if len(tokens) > 1:
                filesystem.load_state(tokens[1])
            else:
                print("Error: Missing file path for load_state command.")
        elif operation == 'exit':
            break
        else:
            print("Invalid command. Try again.")
