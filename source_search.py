import requests
import re
from colorama import init, Fore

# Initialize colorama
init()

def check_domain_in_blocklist(source_url, target_domain):
    try:
        response = requests.get(source_url)
        response.raise_for_status()

        lines = [line.strip() for line in response.text.split('\n') if line.strip() and not line.startswith(('#', '!'))]

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

    except requests.exceptions.RequestException as e:
        print(f"Error checking {source_url}: {e}")

    # Return an empty list if there's an error
    return []

def find_blocking_blocklists(target_domain, green_sources, blue_sources, search_sources):
    blocking_green_blocklists = []
    blocking_blue_blocklists = []

    for name, source in green_sources.items():
        if search_sources in ('g', 'green', 'green sources', 'a', 'all') and check_domain_in_blocklist(source, target_domain):
            blocking_green_blocklists.append(name)

    for name, source in blue_sources.items():
        if search_sources in ('b', 'blue', 'blue sources', 'a', 'all') and check_domain_in_blocklist(source, target_domain):
            blocking_blue_blocklists.append(name)

    if search_sources in ('g', 'green', 'green sources', 'a', 'all') and blocking_green_blocklists:
        print(Fore.GREEN + f"Domain '{target_domain}' found in the following green sources:\n")
        for blocklist in blocking_green_blocklists:
            print(Fore.GREEN + f" - {blocklist}\n")

    if search_sources in ('b', 'blue', 'blue sources', 'a', 'all') and blocking_blue_blocklists:
        print(Fore.BLUE + f"Domain '{target_domain}' found in the following blue sources:\n")
        for blocklist in blocking_blue_blocklists:
            print(Fore.BLUE + f" - {blocklist}\n")

    if not blocking_green_blocklists and not blocking_blue_blocklists:
        print(Fore.RED + f"Domain '{target_domain}' not found in any sources.")

    # Reset the text color to default
    print(Fore.RESET, end='')

if __name__ == "__main__":
    green_blocklist_sources = {
        'KADhosts (Suspicious)': 'https://raw.githubusercontent.com/FiltersHeroes/KADhosts/master/KADomains.txt',
        'Add.Spam (Suspicious)': 'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts',
        'WaLLy3K List (Suspicious)': 'https://v.firebog.net/hosts/static/w3kbl.txt',
        'Adaway (Ads)': 'https://adaway.org/hosts.txt',
        'GetAdmiral Domains (Ads)': 'https://raw.githubusercontent.com/LanikSJ/ubo-filters/main/filters/getadmiral-domains.txt',
        'anudeepND List (Ads)': 'https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt',
        'Pete Lowe List (Ads)': 'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=1&mimetype=plaintext',
        'Unchecky (Ads)': 'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts',
        'hostsVN (Ads)': 'https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts',
        'Adguard DNS Filter (Ads/Tracking)': 'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt',
        'Prigent Ads (Tracking)': 'https://v.firebog.net/hosts/Prigent-Ads.txt',
        'Add.2o7Net (Tracking)': 'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts',
        'Windows Spy List (Tracking)': 'https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt',
        'Geoffrey Frogeye First-Party Trackers (Tracking)': 'https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt',
        'DandelionSprout AntiMalware (Malicious)': 'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt',
        'Threat Intel List (Malicious)': 'https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt',
        'Prigent Crypto (Malicious)': 'https://v.firebog.net/hosts/Prigent-Crypto.txt',
        'Add.Risk (Malicious)': 'https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts',
        'Mandiant_APT1_Report_Appendix_D (Malicious)': 'https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt',
        'Phishing Army (Malicious)': 'https://phishing.army/download/phishing_army_blocklist_extended.txt',
        'Quidsup Malware (Malicious)': 'https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/malware.hosts',
        'RPiList Malware (Malicious)': 'https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware',
        'RPiList Phishing (Malicious)': 'https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe',
        'Spam404 (Malicious)': 'https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt',
        'Stalkerware Indicators (Malicious)': 'https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts_full',
        'URLHaus Malware (Malicious)': 'https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-hosts.txt',
        'ZeroDot1 CoinBlocker (Exclusive)': 'https://gitlab.com/ZeroDot1/CoinBlockerLists/-/raw/master/hosts',
    }

    blue_blocklist_sources = {
        'Referrer Spam (Suspicious)': 'https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt',
        'Dan Pollock Hosts (Suspicious)': 'https://someonewhocares.org/hosts/zero/hosts',
        'VeleSila Hosts (Suspicious)': 'https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts',
        'MVPS Hosts (Suspicious)': 'https://winhelp2002.mvps.org/hosts.txt',
        'neoFelhz neoHosts (Suspicious)': 'https://cdn.jsdelivr.net/gh/neoFelhz/neohosts@gh-pages/full/hosts.txt',
        'RooneyMcNibNug SNAFU (Suspicious)': 'https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt',
        'BarbBlock List (Suspicious)': 'https://raw.githubusercontent.com/paulgb/BarbBlock/main/blocklists/ublock-origin.txt',
        'The Hosts File Project (Bog Only)': 'https://hostsfile.mine.nu/hosts0.txt',
        'Mahakala (Bog Only)': 'https://adblock.mahakala.is/',
        'Jdlingyu Ad-wars (Ads)': 'https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts',
        'Lightswitch05 Ads Tracking (Tracking)': 'https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt',
        'Perflyst Android Trackers (Tracking)': 'https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt',
        'Perflyst SmartTV Domains (Tracking)': 'https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt',
        'Perflyst Amazon FireTV Domains (Tracking)': 'https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt',
        'Quidsup Tracker (Tracking)': 'https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/trackers.hosts',
        'Geoffrey Frogeye Multi-Party Trackers (Bog Only)': 'https://hostfiles.frogeye.fr/multiparty-trackers-hosts.txt',
        'Kees1958 Top Ads Trackers (Bog Only)': 'https://raw.githubusercontent.com/Kees1958/W3C_annual_most_used_survey_blocklist/master/EU_US_MV3_most_common_ad%2Btracking_networks.txt',
        'Phishing Blocklist (Malicious)': 'https://malware-filter.gitlab.io/malware-filter/phishing-filter-agh.txt',
        'Prigent Malware (Malicious)': 'https://v.firebog.net/hosts/Prigent-Malware.txt',
        'Porn List (Exclusive)': 'https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list',
        'Personal List (Bog Only)': 'https://raw.githubusercontent.com/KnightmareVIIVIIXC/AdGuard-Home-Allowlist/main/personal_disallowed_domains.txt',
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

        while True:
            search_option = input("Search in (g)reen, (b)lue, or (a)ll sources? ").lower()

            if search_option == 'reset':
                break  # Break to the outer loop and start over
            elif search_option in ('g', 'green', 'green sources', 'b', 'blue', 'blue sources', 'a', 'all'):
                find_blocking_blocklists(target_domain, green_blocklist_sources, blue_blocklist_sources, search_option)
                break
            else:
                print(Fore.YELLOW + "Invalid reply")
                print(Fore.RESET, end='')
