
# ⭕ The Firebog • DNS Blocklists ⭕

[![](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/assets/114373431/def0ccf3-6b0d-4cfe-91ca-1225f85da364)
](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/LICENSE)


Diverse DNS blocklists crafted from an amalgamation of [sources](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/sources.md) that will

- Hide Advertisements

- Halt Trackers

- Block Malicious Websites

- Stop Phishing Attempts

- Disable Crypto Miners

- Prevent [NSFW](https://www.howtogeek.com/438957/what-does-nsfw-mean-and-how-do-you-use-it/) Content

---

# 🔴 The Lists 🔴

Blocklists converted into [adblock syntax](https://adguard-dns.io/kb/general/dns-filtering-syntax/#adblock-style-syntax) • [hosts syntax](https://adguard-dns.io/kb/general/dns-filtering-syntax/#etc-hosts-syntax) • [domain-only syntax](https://adguard-dns.io/kb/general/dns-filtering-syntax/#domains-only-syntax)

> [!IMPORTANT]
> The lists are built to be used with
> - AdBlockers ([uBlock Origin](https://ublockorigin.com/) • [Adguard](https://adguard.com/en/welcome.html) • [etc.](https://alternativeto.net/software/adguard/))
>
> - Hosts Files
>
> - DNS Applications ([Pi-Hole](https://docs.pi-hole.net) • [Adguard Home](https://adguard.com/en/adguard-home/overview.html) • [etc.](https://alternativeto.net/software/adguard-home/))
>
>> - Find more information [here](https://github.com/fabriziosalmi/blacklists/blob/main/docs/Introduction.md#dns-based-filtering)

| List | ⬜ | Description |
|---:|:---:|:---|
|Bog| 🟧 |Incorporates all sources • contains false positives|
|Blue/Green| 🔶 |Incorporates blue/green sources • poses a high risk of containing false positives|
|Blue| 🟦 |Incorporates blue sources • poses a high risk of containing false positives|
|Green| 🟩 |Incorporates green sources • poses a low risk of containing false positives • excludes [anudeepND's Allowlist](https://github.com/KnightmareVIIVIIXC/allowlist)|

> [!CAUTION]  
> Using more than one list at the same time can cause issues

| AIO Lists | ⬜ | AdBlock | Hosts | Domain | 🟩 🟦 🟧 |
|---:|:---:|:---:|:---:|:---:|:---|
| The Bog List | 🟧 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/aiofirebog.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/aiofirebog.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/aiofirebog.txt) | Contains all of the sources |
| Blue/Green List | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/aiofirebogbluegreen.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/aiofirebogbluegreen.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/aiofirebogbluegreen.txt) | Contains all of the blue/green sources |
| Blue List | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/aiofirebogblue.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/aiofirebogblue.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/aiofirebogblue.txt) | Contains all of the blue sources |
| Green List | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/aiofireboggreen.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/aiofireboggreen.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/aiofireboggreen.txt) | Contains all of the green sources |

> [!TIP]
> If an AIO List is causing issues, consider trying one of the Lite Lists
>
>> If a Lite List causes issues, request a [custom blocklist](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/issues/new/choose)

| Blue/Green Lite Lists | ⬜ | AdBlock | Hosts | Domain | 🔶 🔶 🔶 |
|---:|:---:|:---:|:---:|:---:|:---|
| Suspicious-Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogsusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogsusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogsusmal.txt) | Contains the blue/green suspicious • malicious sources |
| Suspicious-Tracking | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogsustrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogsustrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogsustrack.txt) | Contains the blue/green suspicious • tracking sources |
| Advertising-Tracking | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogadtrack.txt) | Contains the blue/green advertising • tracking sources |
| Advertising-Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogadmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogadmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogadmal.txt) | Contains all of the advertising • malicious sources |
| Advertising-Tracking-Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogadtrackmal.txt) | Contains the blue/green advertising • tracking • malicious sources |
| Misc-Suspicious-Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogsusmalother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogsusmalother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogsusmalother.txt) | Contains the blue/green suspicious • malicious • miscellaneous sources |
| Suspicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogsus.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogsus.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogsus.txt) | Contains the blue/green suspicious sources |
| Advertising | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogad.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogad.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogad.txt) | Contains all of the advertising sources |
| Tracking | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogtrack.txt) | Contains the blue/green tracking sources |
| Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogmal.txt) | Contains all of the malicious sources |
| Miscellaneous | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogother.txt) | Contains the blue/green miscellaneous sources |

| Blue Lite Lists | ⬜ | AdBlock | Hosts | Domain | 🟦 🟦 🟦 |
|---:|:---:|:---:|:---:|:---:|:---|
| Suspicious-Malicious | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogbluesusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogbluesusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogbluesusmal.txt) | Contains the blue suspicious • malicious sources |
| Suspicious-Tracking | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogbluesustrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogbluesustrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogbluesustrack.txt) | Contains the blue tracking • suspicious sources |
| Advertising-Tracking | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogblueadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogblueadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogblueadtrack.txt) | Contains the blue advertising • tracking sources |
| Advertising-Tracking-Malicious | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogblueadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogblueadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogblueadtrackmal.txt) | Contains the blue advertising • tracking • malicious sources |
| Misc-Suspicious | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogbluesusother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogbluesusother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogbluesusother.txt) | Contains the blue suspicious • miscellaneous sources |

| Green Lite Lists | ⬜ | AdBlock | Hosts | Domain | 🟩 🟩 🟩 |
|---:|:---:|:---:|:---:|:---:|:---|
| Suspicious-Malicious | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreensusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreensusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreensusmal.txt) | Contains the green suspicious • malicious sources |
| Advertising-Tracking | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreenadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreenadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreenadtrack.txt) | Contains the green advertising • tracking sources |
| Advertising-Malicious | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreenadmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreenadmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreenadmal.txt) | Contains the green advertising • malicious sources |
| Advertising-Tracking-Malicious | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreenadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreenadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreenadtrackmal.txt) | Contains the green advertising • tracking • malicious sources |
| Misc-Malicious | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreenmalother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreenmalother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreenmalother.txt) | Contains the green malicious • miscellaneous sources |

---

## [👨‍💻](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/category_search.py) The Tests [👩‍💻](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/source_search.py)

Use these to identify what is being blocked by the list of your choice

|🟧|🟩┃🟦┃🟩|🟧|
|:---:|:---:|:---:|
|🟦| [d3ward's Toolz](https://d3ward.github.io/toolz/) |🟦|
|🟩| [AdBlock Tester](https://adblock-tester.com/) |🟩|
|🟦| [Can You Block It](https://canyoublockit.com/) |🟦|
|🟩| [Cover Your Tracks](https://coveryourtracks.eff.org/) |🟩|
|🟧|🟦┃🟩┃🟦|🟧|
