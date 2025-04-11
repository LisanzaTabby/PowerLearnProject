def read_and_write_file():
    # Prompt user for filename
    filename = input("Enter the name of the file to read:")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new file and write the modified content
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to: {new_filename}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: Could not read the file.")

# Run the program
read_and_write_file()
