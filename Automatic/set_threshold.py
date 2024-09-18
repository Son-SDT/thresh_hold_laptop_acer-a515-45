import sys
import controller as ctl
fc = ctl.function()

def replace_value_in_file(file_path, number):
    try:
        # Read the current content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace the value in the content
        with open(file_path, 'w') as file:
            for line in lines:
                # Replace the placeholder with the given number
                if 'value_to_replace=' in line:
                    line = f'value_to_replace={number}\n'
                file.write(line)
                
        print(f"Value replaced with {number} in {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python set.py <number>")
        sys.exit(1)

    number = sys.argv[1]
    if not number.isdigit():
        print("Error: The argument must be a number.")
        sys.exit(1)

    file_path = f'{fc.get_current_dir()}/config.txt'
    replace_value_in_file(file_path, number)

if __name__ == "__main__":
    main()
