import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import teams 
from time import sleep, time
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)"
]
all_data = []
failed_teams = []

def get_html(url, retries=3, wait=3):
    i = 0
    for attempt in range(retries):
        headers = {"User-Agent": USER_AGENTS[i]}
        i += 1
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, "html.parser")
            if soup.find_all("tr", class_=["odd", "even"]):
                return soup
        print(f"Will retry: {url}")
        sleep(wait + random.uniform(0.5, 2))
    return None

def get_team_data(club_name, club_id):
    url = f"https://www.transfermarkt.com.tr/{club_name}/kader/verein/{club_id}/saison_id/2025/plus/1"
    soup = get_html(url)
    if not soup:
        return False
    
    rows = soup.find_all("tr", class_=["odd", "even"])
    for item in rows:
        td = item.find("td", class_="hauptlink")
        position = item.find_all("tr")[1].text.strip() if item.find_all("tr") and len(item.find_all("tr")) > 1 else None
        player = td.find("a").text.strip() if td and td.find("a") else None
        info = item.find_all("td", {"class": "zentriert"}) if item.find("td", {"class": "zentriert"}) else None
        number = info[0].text.strip() if info and len(info) > 0 else None
        age = info[1].text.strip().split("(")[1].replace(")", "").strip() if info and len(info) > 1 else None
        country = info[2].find("img")["title"].strip() if info and len(info) > 2 and info[2].find("img") else None
        height = info[3].text.strip() if info and len(info) > 3 else None
        foot = info[4].text.strip() if info and len(info) > 4 else None
        value = item.find("td", {"class": "rechts hauptlink"}).text.strip() if item.find("td", {"class": "rechts"}) else None
        previous_team = info[6].find("img")["alt"].strip() if info and len(info) > 6 and info[6].find("img") else None
        transfer_fee = info[6].find("a")["title"].strip() if info and len(info) > 6 and info[6].find("a") else None
        transfer_fee = re.search(r"Ablöse\s*(.*)", transfer_fee).group(1) if transfer_fee else None
        status = item.find_all('a')[1].find('img')["src"].strip() if item.find_all('a') and item.find_all('a')[1].find('img') else None
        if status == "/images/icons/leihe_beta_kader.png":
            status = "Loan"
        else:
            status = "Permanent"

        all_data.append({
            "Player": player,
            "Number": number,
            "Position": position,
            "Team": club_name,
            "Age": age,
            "Country": country,
            "Height": height,
            "Foot": foot,
            "Value": value,
            "Previous Team": previous_team,
            "Transfer Fee": transfer_fee,
            "Status": status
        })
    return True

start_time = time()

# First attempt
for index, team in teams.teams.iterrows():
    print(f"📥 Fetching {team['Club Name']}...")
    if not get_team_data(team['Club Name'], team['Club ID']):
        failed_teams.append((team['Club Name'], team['Club ID']))
    sleep(3 + random.uniform(0.5, 1.5))

# Second attempt
if failed_teams:
    print("\n🔄 Retrying failed teams...")
    retry_list = failed_teams.copy()
    failed_teams.clear()
    for club_name, club_id in retry_list:
        print(f"📥 (Retry) Fetching {club_name}...")
        if not get_team_data(club_name, club_id):
            failed_teams.append((club_name, club_id))
        sleep(3 + random.uniform(0.5, 1.5))

# Save results
df = pd.DataFrame(all_data)
df.to_csv("Players.csv", index=False)
# Total time 
end_time = time()
total_time = end_time - start_time
minutes = int(total_time // 60)
seconds = total_time % 60
print(f"\n⏳ Total time: {minutes} minutes {seconds:.2f} seconds")

# Still failed teams
if failed_teams:
    print("\n❌ Still failed teams:")
    for team in failed_teams:
        print(team)
