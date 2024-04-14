# Booking.com-Scraper

This Python script uses Playwright to scrape hotel information from Booking.com for a stay in Los Angeles, CA from 12/01/2024 - 12/08/2024. It retrieves data such as hotel name, price, review score, and review count, and saves it to both Excel and CSV files. Potential improvements include allowing users to enter their city and dates of choice, along with the relevant exception handling.

## Requirements

- Python 3.x
- Playwright
- Pandas

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install Playwright: `pip install playwright`.
3. Install Pandas: `pip install pandas`.

## Usage

1. Set the desired check-in and check-out dates in the `checkin_date` and `checkout_date` variables in the `main()` function.
2. Run the script: `python scraper.py`.

## Output

The script generates two output files:
- `hotels_list.xlsx`: Excel file containing the scraped hotel data.
- `hotels_list.csv`: CSV file containing the scraped hotel data.
