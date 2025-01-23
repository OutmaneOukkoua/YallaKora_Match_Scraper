import requests
from bs4 import BeautifulSoup
import csv

date = input("Please enter a Date in the following format MM/DD/YYYY: ")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []
    championships = soup.find_all("div", {'class': 'matchCard'})

    def get_match_info(championship):
        championship_title = championship.contents[1].find("h2").text.strip()
        all_matches = championship.find_all("div", {'class': 'item future liItem'})

        for match in all_matches:
            # get teams names
            team_A = match.find("div", {'class': 'teamA'}).text.strip()
            team_B = match.find("div", {'class': 'teamB'}).text.strip()

            # get match result
            match_result = match.find("div", {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            # get match time
            match_time = match.find("div", {'class': 'MResult'}).find('span', {'class': 'time'}).text.strip()

            # add match info to matches_details list
            matches_details.append(
                {
                    'meisterschaftstyp': championship_title,
                    'erstemanschaft': team_A,
                    'zweitemanschaft': team_B,
                    'Fußballergebnis': score,
                    'Fußballspielzeit': match_time
                }
            )

    for champ in championships:
        get_match_info(champ)

    # Safely handle the case where there might be no matches found
    if not matches_details:
        print("No matches found for the specified date.")
        return

    keys = matches_details[0].keys()

    # Specify UTF-8 encoding to avoid UnicodeEncodeError
    with open('matches-details.csv', 'w', encoding='utf-8-sig', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("File created successfully!")

main(page)
