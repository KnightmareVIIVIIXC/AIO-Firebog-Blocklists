
# ⭕ The Firebog • DNS Blocklists ⭕

[![](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/assets/114373431/def0ccf3-6b0d-4cfe-91ca-1225f85da364)
](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/LICENSE)

Diverse DNS blocklists crafted from an amalgamation of sources<br>that are intended to
- Hide Advertisements
- Halt Trackers
- Block Malicious Content
- Stop Phishing Attempts
- Disable Crypto Miners
- Prevent Adult Content

---

## 🔴 The Lists 🔴

Blocklists designed in the syntax of [adblock](https://adguard-dns.io/kb/general/dns-filtering-syntax/#adblock-style-syntax), [hosts](https://adguard-dns.io/kb/general/dns-filtering-syntax/#etc-hosts-syntax), & [domain-only](https://adguard-dns.io/kb/general/dns-filtering-syntax/#domains-only-syntax)
<br>that are meant to be used with
- AdBlockers (uBlock Origin, Adguard, etc.)
- Hosts Files
- DNS Applications (Pi-Hole, Adguard Home, etc.)

> [!IMPORTANT]
> These lists use sources found on [The Firebog](https://v.firebog.net) by [WaLLy3K](https://github.com/WaLLy3K)
> 
> The lists are compiled using [HostlistCompiler](https://github.com/AdguardTeam/HostlistCompiler) by [AdguardTeam](https://github.com/AdguardTeam)

| List | ⬜ | Description |
|---:|:---:|:---|
|Bog| 🟧 |Incorporates all sources, contains false positives|
|Blue/Green| 🔶 |Incorporates blue sources & green sources, poses a high risk of containing false positives|
|Blue| 🟦 |Incorporates blue sources, poses a high risk of containing false positives|
|Green| 🟩 |Incorporates green sources, poses a low risk of containing false positives, excludes [anudeepND's Allowlist](https://github.com/KnightmareVIIVIIXC/allowlist)|

> [!CAUTION]  
> Using more than one list at the same time can cause issues

| AIO Lists | ⬜ | AdBlock | Hosts | Domain | 🟩 🟦 🟧 |
|---:|:---:|:---:|:---:|:---:|:---|
| The Bog List | 🟧 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/aiofirebog.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/aiofirebog.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/aiofirebog.txt) | Contains all of the sources |
| Blue/Green List | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/aiofirebogbluegreen.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/aiofirebogbluegreen.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/aiofirebogbluegreen.txt) | Contains all of the blue/green sources |
| Blue List | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/aiofirebogblue.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/aiofirebogblue.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/aiofirebogblue.txt) | Contains all of the blue sources |
| Green List | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/aiofireboggreen.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/aiofireboggreen.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/aiofireboggreen.txt) | Contains all of the green sources |

> [!TIP]
> If an AIO list is too much, try one of the Lite Lists

| Lite Lists | ⬜ | 🔶 | 🔶 | 🔶 | 🔶 🔶 🔶 |
|---:|:---:|:---:|:---:|:---:|:---|
| Suspicious-Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogsusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogsusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogsusmal.txt) | Contains the blue/green suspicious & malicious sources |
| Suspicious-Tracking | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogsustrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogsustrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogsustrack.txt) | Contains the blue/green suspicious & tracking sources |
| Advertising-Tracking | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogadtrack.txt) | Contains the blue/green advertising & tracking sources |
| Advertising-Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogadmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogadmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogadmal.txt) | Contains all of the advertising & malicious sources |
| Advertising-Tracking-Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogadtrackmal.txt) | Contains the blue/green advertising, tracking, & malicious sources |
| Misc-Suspicious-Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogsusmalother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogsusmalother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogsusmalother.txt) | Contains the blue/green suspicious, malicious, & miscellaneous sources |
| Suspicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogsus.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogsus.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogsus.txt) | Contains the blue/green suspicious sources |
| Advertising | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogad.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogad.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogad.txt) | Contains all of the advertising sources |
| Tracking | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogtrack.txt) | Contains the blue/green tracking sources |
| Malicious | 🔶 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogmal.txt) | Contains all of the malicious sources |
| 🟦 🟦 🟦 | ⬜ | 🟦 | 🟦 | 🟦 | 🟦 🟦 🟦 |
| Suspicious-Malicious | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogbluesusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogbluesusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogbluesusmal.txt) | Contains the blue suspicious & malicious sources |
| Suspicious-Tracking | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogbluesustrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogbluesustrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogbluesustrack.txt) | Contains the blue tracking & suspicious sources |
| Advertising-Tracking | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogblueadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogblueadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogblueadtrack.txt) | Contains the blue advertising & tracking sources |
| Advertising-Tracking-Malicious | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogblueadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogblueadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogblueadtrackmal.txt) | Contains the blue advertising, tracking, & malicious sources |
| Misc-Suspicious | 🟦 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/firebogbluesusother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/firebogbluesusother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/firebogbluesusother.txt) | Contains the blue suspicious & miscellaneous sources |
| 🟩 🟩 🟩 | ⬜ | 🟩 | 🟩 | 🟩 | 🟩 🟩 🟩 |
| Suspicious-Malicious | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreensusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreensusmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreensusmal.txt) | Contains the green suspicious & malicious sources |
| Advertising-Tracking | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreenadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreenadtrack.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreenadtrack.txt) | Contains the green advertising & tracking sources |
| Advertising-Malicious | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreenadmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreenadmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreenadmal.txt) | Contains the green advertising & malicious sources |
| Advertising-Tracking-Malicious | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreenadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreenadtrackmal.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreenadtrackmal.txt) | Contains the green advertising, tracking, & malicious sources |
| Misc-Malicious | 🟩 | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/lists/fireboggreenmalother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/hostslists/fireboggreenmalother.txt) | [RAW](https://raw.githubusercontent.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/main/domlists/fireboggreenmalother.txt) | Contains the green malicious & miscellaneous sources |

> [!NOTE]
> Lists are updated Monday-Friday, between 01:00-03:00 & 13:00-15:00
>> If they don't, something's wrong 🛠️

---

## [🔥](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/category_search.py) [The](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/category_search.py) [Sources](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/source_search.py) [🔥](https://github.com/KnightmareVIIVIIXC/AIO-Firebog-Blocklists/blob/main/source_search.py)

| List | ⬜ | Description |
|---:|:---:|:---|
|Bog| 🟧 |Exclusive to The Bog All-In-One (AIO) list|
|Blue| 🟦 |Featured in The Bog AIO list & blue lists|
|Green| 🟩 |Featured in The Bog AIO list & green lists|

| ⬜ ⬜ ⬜ | ⬜ | Source |
|---:|:---:|:---|
| Suspicious | ⬜ | 🟩 🟦 🟧 |
| ⬛ | 🟩 | [WaLLy3K's Blocklist](https://v.firebog.net/hosts/static/w3kbl.txt) |
| ⬛ | 🟩 | [PolishFiltersTeam KADhosts](https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt) |
| ⬛ | 🟩 | [Fademind's Spammers](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts) |
| ⬛ | 🟦 | [Matomo Referrer Spam](https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt) |
| ⬛ | 🟦 | [Dan Pollock's List](https://someonewhocares.org/hosts/zero/hosts) |
| ⬛ | 🟦 | [VeleSila yhosts](https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts) |
| ⬛ | 🟦 | [MVPS Hosts](https://winhelp2002.mvps.org/hosts.txt) |
| ⬛ | 🟦 | [neoFelhz's neoHosts](https://cdn.jsdelivr.net/gh/neoFelhz/neohosts@gh-pages/full/hosts.txt) |
| ⬛ | 🟦 | [RooneyMcNibNug's SNAFU list](https://raw.githubusercontent.com/RooneyMcNibNug/pihole-stuff/master/SNAFU.txt) |
| ⬛ | 🟦 | [paulgb's BarbBlock](https://paulgb.github.io/BarbBlock/blacklists/domain-list.txt) |
| ⬛ | 🟧 | [The Hosts File Project](https://hostsfile.mine.nu/hosts0.txt) |
| ⬛ | 🟧 | [Mahakala](https://adblock.mahakala.is/) |
| Advertising | ⬜ | 🟩 🟦 ⬛ |
| ⬛ | 🟩 | [AdAway](https://adaway.org/hosts.txt) |
| ⬛ | 🟩 | [LanikSJ's GetAdmiral](https://raw.githubusercontent.com/LanikSJ/ubo-filters/main/filters/getadmiral-domains.txt) |
| ⬛ | 🟩 | [Anudeep ND's Blocklist](https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt) |
| ⬛ | 🟩 | [Peter Lowe's Adservers](https://pgl.yoyo.org/adservers/serverlist.php?hostformat=nohtml) |
| ⬛ | 🟩 | [Fademind's Unchecky Ads](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts) |
| ⬛ | 🟩 | [hostsVN](https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts) |
| ⬛ | 🟦 | [Jdlingyu's Ad-wars](https://raw.githubusercontent.com/jdlingyu/ad-wars/master/hosts) |
| Advertising/Tracking | ⬜ | 🟩 ⬛ ⬛ |
| ⬛ | 🟩 | [AdGuard DNS Filter](https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt) |
| Tracking | ⬜ | 🟩 🟦 🟧 |
| ⬛ | 🟩 | [Fabrice Prigent's Ads](https://v.firebog.net/hosts/Prigent-Ads.txt) |
| ⬛ | 🟩 | [Fademind's 2o7 Network Trackers](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts) |
| ⬛ | 🟩 | [Crazy Max's Microsoft Telemetry](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt) |
| ⬛ | 🟩 | [Geoffrey Frogeye's First-Party Trackers](https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt) |
| ⬛ | 🟦 | [Lightswitch05's Ads & Tracking](https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt) |
| ⬛ | 🟦 | [Perflyst's Android Trackers](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt) |
| ⬛ | 🟦 | [Perflyst's SmartTV Domains](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt) |
| ⬛ | 🟦 | [Perflyst's Amazon FireTV Domains](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt) |
| ⬛ | 🟦 | [Quidsup NoTrack Tracker Blocklist](https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt) |
| ⬛ | 🟧 | [Geoffrey Frogeye's Multi-Party Trackers](https://hostfiles.frogeye.fr/multiparty-trackers-hosts.txt) |
| ⬛ | 🟧 | [Kees1958's Top Ads & Trackers](https://github.com/Kees1958/W3C_annual_most_used_survey_blocklist/blob/master/EU_US_MV2_most_common_ad%2Btracking_networks.txt) |
| Malicious | ⬜ | 🟩 🟦 ⬛ |
| ⬛ | 🟩 | [DandelionSprout's Anti-Malware Filter](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt) |
| ⬛ | 🟩 | [DigitalSide Threat-Intel](https://osint.digitalside.it/Threat-Intel/lists/latestdomains.txt) |
| ⬛ | 🟩 | [Fabrice Prigent's Cryptojacking](https://v.firebog.net/hosts/Prigent-Crypto.txt) |
| ⬛ | 🟩 | [Fademind's Risky Hosts](https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts) |
| ⬛ | 🟩 | [Mandiant APT1 Report](https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt) |
| ⬛ | 🟩 | [Phishing Army's Extended Blocklist](https://phishing.army/download/phishing_army_blocklist_extended.txt) |
| ⬛ | 🟩 | [Quidsup NoTrack Malware Blocklist](https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt) |
| ⬛ | 🟩 | [RPiList Malware](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/malware) |
| ⬛ | 🟩 | [RPiList Phishing](https://raw.githubusercontent.com/RPiList/specials/master/Blocklisten/Phishing-Angriffe) |
| ⬛ | 🟩 | [Spam404](https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt) |
| ⬛ | 🟩 | [AssoEchap's Stalkerware Indicators](https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts) |
| ⬛ | 🟩 | [URLhaus Malware URL blocklist](https://urlhaus.abuse.ch/downloads/hostfile/) |
| ⬛ | 🟦 | [Curbengh's Phishing filter](https://malware-filter.gitlab.io/malware-filter/phishing-filter-hosts.txt) |
| ⬛ | 🟦 | [Fabrice Prigent's Malware](https://v.firebog.net/hosts/Prigent-Malware.txt) |
| Miscellaneous | ⬜ | 🟩 🟦 🟧 |
| ⬛ | 🟩 | [ZeroDot1 CoinBlockerLists](https://gitlab.com/ZeroDot1/CoinBlockerLists/-/raw/master/hosts) |
| ⬛ | 🟦 | [Chad Mayfield (Top 1M)](https://raw.githubusercontent.com/chadmayfield/my-pihole-blocklists/master/lists/pi_blocklist_porn_top1m.list) |
| ⬛ | 🟧 | [Anudeep ND's Facebook Blocklist](https://raw.githubusercontent.com/anudeepND/blacklist/master/facebook.txt) |

---

## 👨‍💻 The Tests 👨‍💻

Identify what is being blocked by the list of your choice

|🟧|🟩┃🟦┃🟩|🟧|
|:---:|:---:|:---:|
|🟦| [d3ward's Toolz](https://d3ward.github.io/toolz/) |🟦|
|🟩| [AdBlock Tester](https://adblock-tester.com/) |🟩|
|🟦| [Can You Block It](https://canyoublockit.com/) |🟦|
|🟩| [Cover Your Tracks](https://coveryourtracks.eff.org/) |🟩|
|🟧|🟦┃🟩┃🟦|🟧|
