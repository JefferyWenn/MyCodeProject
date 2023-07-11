"""
File: webcrawler.py
Name: 溫孟哲
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
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        male_total = 0
        female_total = 0
        i = 2
        for tag in tags:
            while i <= 1000:
                male_num = int(tag.text.split()[i].replace(',', ''))
                male_total += male_num
                female_num = int(tag.text.split()[i+2].replace(',', ''))
                female_total += female_num
                i += 5
        print("Male number: "+str(male_total))
        print("Female number: "+str(female_total))


if __name__ == '__main__':
    main()
