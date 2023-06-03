# CodeScribe

CodeScribe is an automated tool that generates beginner-friendly, professional multiline comments to accompany code without making any changes to the code itself. It simplifies the process of documenting code by providing descriptive comments based on the code's functionality.

## Features

- Generate descriptive comments for code files in a specified folder.
- Supports various programming languages.
- Beginner-friendly and professional comment generation.
- Does not modify the code files.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- OpenAI API key

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/TheZenithCo/CodeScribe.git
   ```

2. Install the required Python dependencies:

   ```
   pip install -r requirements.txt
   ```

### Usage

1. Provide your OpenAI API key in the `config.py` file.

2. Run the `CodeScriber.py` script with the path to the code folder as a command-line argument:

   ```
   python CodeScribe.py /path/to/code_folder
   ```

   Replace `/path/to/code_folder` with the actual path to the folder containing your code files.

3. Select the file number to display the code.

4. CodeScribe will generate descriptive comments for the displayed code file and print them to the console.

5. You can copy and paste the generated comments into the corresponding code files as needed.

## Contributing

Contributions to CodeScribe are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

Before contributing, please review the [contribution guidelines](CONTRIBUTING.md).

## License

CodeScribe is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The CodeScribe project was inspired by the need to simplify and automate code documentation.
- Thanks to the OpenAI team for providing the powerful text generation capabilities used in this project.

## Contact

For any inquiries or questions, please reach out to [0xAdiyat@gmail.com](mailto:0xAdiyat@gmail.com).

Enjoy using CodeScribe!
