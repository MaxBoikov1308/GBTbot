import sys

def get_api_key():
    print("Enter your API key:")
    api_key = sys.stdin.readline().strip()
    return api_key