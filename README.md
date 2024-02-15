
# Password Generator

This is a Python script that generates passwords of varying lengths using a specified character set and saves them to a file.

## Features

- Allows users to specify minimum and maximum password lengths.
- Supports custom character sets in addition to the default set of ASCII letters, digits, and special characters.
- Dynamically displays progress as passwords are generated.
- Provides error handling for file operations and user input validation.

## Usage

1. Clone the repository:


2. Navigate to the project directory:

3. Run the script:


4. Follow the prompts to specify the password length range, file path for saving passwords, and character set preferences.

## Memory Estimate

The memory usage of the script mainly depends on the number of passwords generated and the length of each password. Here's a rough estimate:

- Each character in the password takes up 1 byte (assuming ASCII characters).
- Let's assume the average length of passwords generated is 12 characters.
- If you generate 1 million passwords, the memory usage would be approximately 12 MB.

Actual memory usage may vary depending on factors such as system resources and Python interpreter overhead.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
