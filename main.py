import argparse
import os.path
import sys

parser = argparse.ArgumentParser(description="CodeScribe - An Automate way to describe code")

if len(sys.argv) < 2:
    print("Usage: python CodeScriber.py /code_folder")
    sys.exit(1)

code_folder = sys.argv[1]

if not os.path.isdir(code_folder):
    print(f"Invalid code folder path: {code_folder}")
    sys.exit(1)
