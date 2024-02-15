import itertools
import string
import os

def generate_passwords(min_length, max_length, file_path, characters):
    try:
        # Open the file using a context manager
        with open(file_path, 'w') as file:
            # Calculate the total number of combinations
            total_combinations = sum(len(characters) ** length for length in range(min_length, max_length + 1))
            # Determine an optimal chunk size for performance
            chunk_size = min(total_combinations // 100, 1000000)

            # Loop through the lengths of passwords
            for length in range(min_length, max_length + 1):
                # Generate all combinations of characters of the current length
                all_combinations = itertools.product(characters, repeat=length)
                
                # Write passwords to file in chunks
                for i, combination in enumerate(all_combinations, 1):
                    password = ''.join(combination)
                    file.write(password + '\n')
                    
                    # Print progress dynamically
                    if i % chunk_size == 0 or (i == total_combinations and total_combinations <= chunk_size):
                        print(f"Progress: {i}/{total_combinations}", end='\r')
            
            # Print completion message
            print("\nPasswords have been generated and saved to:", file_path)
    
    # Handle file-related errors
    except IOError:
        print("Error: Cannot write to file at the specified path.")

def get_integer_input(prompt, min_val, max_val):
    # Validate and return user input as an integer within the specified range
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Input must be between {min_val} and {max_val}. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_characters():
    # Allow the user to choose between default and custom character sets
    default_characters = string.ascii_letters + string.digits + '@#%&*$'
    use_default = input("Use default character set? (Y/N): ").strip().lower() == 'y'
    return default_characters if use_default else input("Enter custom character set: ").strip()

if __name__ == "__main__":
    # Get user input for password generation
    min_length = get_integer_input("Enter minimum password length: ", 1, 1000)
    max_length = get_integer_input("Enter maximum password length: ", min_length, 1000)
    
    # Validate and get file path for saving passwords
    file_path = input("Enter the file path to save passwords (e.g., /home/bhanu/Desktop/password.txt): ").strip()
    if not file_path:
        print("Error: File path cannot be empty.")
    else:
        # Get character set from the user
        characters = get_characters()
        print(f"\nGenerating passwords ({min_length}-{max_length} characters)...")
        
        # Generate passwords and save them to the file
        generate_passwords(min_length, max_length, file_path, characters)
