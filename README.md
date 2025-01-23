# YallaKora Match Scraper

This project is a Python script that scrapes football match information from the YallaKora website for a specified date and saves the details to a CSV file. The script uses the `requests`, `BeautifulSoup` (from `bs4`), and `csv` libraries.

## Features

- Scrapes match details (team names, match results, and match times) for a given date from the YallaKora website.
- Organizes match details by championship.
- Saves the scraped data to a CSV file named `matches-details.csv`.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.7 or later
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/yallakora-match-scraper.git
```

2. Navigate to the project directory:

```bash
cd yallakora-match-scraper
```

3. Run the script:

```bash
python scraper.py
```

4. Enter a date in the `MM/DD/YYYY` format when prompted. For example:

```text
Please enter a Date in the following format MM/DD/YYYY: 01/23/2025
```

5. If matches are found, the script will create a CSV file named `matches-details.csv` in the same directory. If no matches are found for the entered date, a message will be displayed.

## Output

The CSV file will contain the following columns:

- `meisterschaftstyp`: The championship type.
- `erstemanschaft`: The name of the first team.
- `zweitemanschaft`: The name of the second team.
- `Fußballergebnis`: The match score.
- `Fußballspielzeit`: The match time.

## Example Output

Here is an example of the CSV output:

```csv
meisterschaftstyp,erstemanschaft,zweitemanschaft,Fußballergebnis,Fußballspielzeit
Championship 1,Team A,Team B,1 - 2,15:00
Championship 1,Team C,Team D,0 - 0,17:30
```

## Notes

- The script relies on the structure of the YallaKora website. If the website's structure changes, the script may need to be updated.
- Ensure you have an active internet connection when running the script.

## Contributions

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the script.

## Disclaimer

This script is intended for educational purposes only. Scraping websites may violate their terms of service. Please use responsibly.
