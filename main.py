import argparse
import os.path
import sys
import pkg_resources
import subprocess
import tiktoken
import openai
from config import API_KEY

required_packages = [
    'openai',
    'tiktoken',
]


def package_is_installed(package):
    return package in {pkg.key for pkg in pkg_resources.working_set}


# Function to install required packages using pip
def install_packages():
    for package in required_packages:
        if not package_is_installed(package):
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            except subprocess.CalledProcessError:
                return False
    return True


if not install_packages():
    print("Failed to install required packages. Please make sure you have pip installed.")
    sys.exit(1)

parser = argparse.ArgumentParser(description="CodeScribe - An Automate way to describe code")
parser.add_argument('-s', '--code_folder', type=str, help='Path to the code folder')
args = parser.parse_args()

if not args.code_folder:
    parser.print_help()
    sys.exit(1)

if not os.path.isdir(args.code_folder):
    print(f"Invalid code folder path: {args.code_folder}")
    sys.exit(1)

code_folder = args.code_folder
file_list = os.listdir(code_folder)
code_files = {}

print("Files in the code folder:")
for i, file_name in enumerate(file_list, start=1):
    print(f"{i}. {file_name}")

    file_path = os.path.join(code_folder, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            code = file.read()
            code_files[file_name] = code
    else:
        print(f"Skipping {file_name} as it is not a file.")

if not code_files:
    print("No code files found in the code folder.")
    sys.exit(1)

file_number = input("Enter the file number to display the code: ")
try:
    file_number = int(file_number)
    if file_number < 1 or file_number > len(file_list):
        raise ValueError
except ValueError:
    print("Invalid file number.")
    sys.exit(1)

file_name = file_list[file_number - 1]
code = code_files[file_name]

print(f"\nCode for file {file_name}:\n")
print(code)

prompt = f"{code}" \
         f"\n\n\n\n" \
         f"generate beginner-friendly, professional multiline comments to accompany the code without making any " \
         f"changes to the code itself. And add it to the code where it's needed to be added. And must include " \
         f"import section in the response. And make sure to keep the import section at the starting point of the file"


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


token_count = num_tokens_from_string(code, "cl100k_base")
print(f"Number of tokens: {token_count}")

if token_count > 2048:
    print("Sorry, the code has too many tokens to process.")
    sys.exit(1)

openai.api_key = API_KEY
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=2048 - token_count
)

print("\nGenerated comments:")
code_scribe_response = response.choices[0].text
print(code_scribe_response)

output_dir = os.path.join(os.getcwd(), "CodeScribeFiles")
os.makedirs(output_dir, exist_ok=True)

# Save the generated comments to a file
output_file = os.path.join(output_dir, "enhanced.js")  # Make the extention of this file dynamic
with open(output_file, "w") as file:
    file.write(code_scribe_response)

print(f"\nGenerated comments saved to: {output_file}")
