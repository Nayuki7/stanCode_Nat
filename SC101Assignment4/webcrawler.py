"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, features="lxml")

        # ----- Write your code below this line ----- #

        # Try finding the table tag with the class 't-stripe'
        table = soup.find('table', {'class': 't-stripe'})
        if not table:
            print("No table with class 't-stripe' found.")
            continue

        rows = table.find_all('tr')
        male_total, female_total = 0, 0
        for row in rows:
            cells = row.find_all('td')
            # Ensure we have the expected number of cells before trying to access them
            if len(cells) == 5:  # Check if the row has 5 cells, as expected
                male_total += int(cells[2].text.replace(',', ''))
                female_total += int(cells[4].text.replace(',', ''))
            else:
                continue  # Skip rows that do not have the expected number of cells

        print(f"Male Number: {male_total}")
        print(f"Female Number: {female_total}")


if __name__ == '__main__':
    main()


    