import requests
from bs4 import BeautifulSoup
URL = "https://local.oisd.nl/extract/commonly_whitelisted.php"
OUTPUT_FILE = "oisd_commonly_whitelisted.txt"
response = requests.get(URL, timeout=30)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
domains = []
for line in soup.get_text("\n").splitlines():
    line = line.strip().lower()
    if not line:
        continue
    if " " not in line and "." in line:
        domains.append(line)
domains = sorted(set(domains))
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(domains))
print(f"Saved {len(domains)} domains.")