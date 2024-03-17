import os
import requests
import re
from colorama import init, Fore

# Initialize colorama
init()

def check_domain_in_blocklist(source_path, target_domain):
    try:
        with open(source_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip() and not line.startswith(('#', '!'))]

        # Initialize an empty list to store results
        results = []

        # More precise whole word matching with wrap-around and domain separator check
        pattern = rf"\b{target_domain}(?!\.\w+)"  # Negative lookahead with domain separator check
        for line in lines:
            match = re.search(pattern, line, flags=re.MULTILINE)
            if match:
                results.append(True)

        # Return the results list
        return results

    except FileNotFoundError:
        print(f"Error: File '{source_path}' not found.")

    # Return an empty list if there's an error
    return []

def find_blocking_blocklists(target_domain, category_sources):
    blocking_category_blocklists = []

    for name, source_path in category_sources.items():
        if check_domain_in_blocklist(source_path, target_domain):
            blocking_category_blocklists.append(name)

    if blocking_category_blocklists:
        print(Fore.CYAN + f"Domain '{target_domain}' found in the following categories:\n")
        for blocklist in blocking_category_blocklists:
            print(Fore.CYAN + f" - {blocklist}\n")

    if not blocking_category_blocklists:
        print(Fore.RED + f"Domain '{target_domain}' not found in any blocklists.")

    # Reset the text color to default
    print(Fore.RESET, end='')

if __name__ == "__main__":
    category_blocklist_sources = {
        'Suspicious': 'domlists/firebogsus.txt',
        'Advertising': 'domlists/firebogad.txt',
        'Tracking': 'domlists/firebogtrack.txt',
        'Malicious': 'domlists/firebogmal.txt',
    }

    while True:
        target_domain = input("Enter a domain to find (or type 'exit' to close): ")

        if target_domain.lower() == 'exit':
            print("Exiting the script.")
            break

        if '.' not in target_domain or target_domain.startswith('.') or target_domain.endswith('.') or '..' in target_domain:
            print(Fore.YELLOW + "Invalid domain")
            print(Fore.RESET, end='')
            continue

        find_blocking_blocklists(target_domain, category_blocklist_sources)
