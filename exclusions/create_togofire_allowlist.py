import requests
import re
url = "https://raw.githubusercontent.com/TogoFire-Home/AD-Settings/main/Filters/whitelist.txt"
output_file = "togofire_whitelist.txt"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    content = response.text
    lines = content.splitlines()
    processed_lines = []
    for line in lines:
        if not line.startswith('@@||'):
            continue
        line = line.replace('@@||', '')
        line = re.sub(r'\^.*', '', line)
        line = re.sub(r'\$.*', '', line)
        processed_lines.append(line)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(processed_lines))
    print(f"Processed content saved to {output_file}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")