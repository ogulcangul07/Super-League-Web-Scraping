import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.transfermarkt.com.tr/super-lig/startseite/wettbewerb/TR1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers).content
soup = BeautifulSoup(response, 'html.parser')
def team_data():
    club_names=[]
    club_ids = []
    rows = soup.find_all("tr", class_=["odd", "even"])
    i=0
    for row in rows:
        i+=1
        if i<19:
            club_name = row.find("td", class_="hauptlink").text.strip()
            club_id = row.find("td", class_="hauptlink no-border-links")
            club_id = club_id.find("a")["href"].split("/")[4] if club_id and club_id.find("a") else None
            club_names.append(club_name)
            club_ids.append(club_id)
        else:
            break
    return pd.DataFrame({"Club Name": club_names, "Club ID": club_ids})
teams=team_data()


