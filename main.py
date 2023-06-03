import argparse
import os.path
import sys
import pkg_resources
import subprocess
import tiktoken
import openai as openai
from config import API_KEY

# List of required packages
required_packages = [
    'openai',
    'tiktoken',
]


# Function to check if a package is already installed
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


# Install required packages
if not install_packages():
    print("Failed to install required packages. Please make sure you have pip installed.")
    sys.exit(1)

parser = argparse.ArgumentParser(description="CodeScribe - An Automate way to describe code")

parser.add_argument('-s', '--code_folder', type=str, help='Path to the code folder')

args = parser.parse_args()

# Check if the code folder path is provided
if not args.code_folder:
    parser.print_help()
    exit(1)

if len(sys.argv) < 2:
    print("Usage: python CodeScriber.py /code_folder")
    sys.exit(1)

code_folder = sys.argv[1]

# Check if the code folder path is valid
if not os.path.isdir(args.code_folder):
    print(f"Invalid code folder path: {args.code_folder}")
    exit(1)

file_list = os.listdir(args.code_folder)
code_files = {}

print("Files in the code folder:")

for i, file_name in enumerate(file_list, start=1):
    print(f"{i}. {file_name}")

    # Read the code from each file and store it in a variable
    # Check if the item in the code folder is a file
    file_path = os.path.join(args.code_folder, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            code = file.read()
            code_files[file_name] = code
    else:
        print(f"Skipping {file_name} as it is not a file.")

file_number = int(input("Enter the file number to display the code: "))
file_name = file_list[file_number - 1]
code = code_files[file_name]

print(f"\nCode for file {file_name}:\n")
print(code)

prompt = f"{code}" \
         f"\n\n\n\n" \
         f"generate beginner-friendly, professional multiline comments to accompany the code without making any " \
         f"changes to the code itself. And add it to the code where it's needed to be add. And yeah must include " \
         f"import section in the response"


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


token_count = num_tokens_from_string(code, "cl100k_base")
print(f"Number of token: {token_count}")

response = ""

# if token_count <= 2048:
#     openai.api_key = API_KEY
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0,
#         max_tokens=2048,
#
#     )
# else:
#     print(f"Sry text limit is 2048 at once")

# print("\nGenerated comments:")
# code_scribe_response = response.choices[0].text
# print(code_scribe_response)

# Create the "CodeScribe Files" directory
output_dir = os.path.join(os.getcwd(), "CodeScribe Files")
os.makedirs(output_dir, exist_ok=True)
