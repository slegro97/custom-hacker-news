import requests
from bs4 import BeautifulSoup as bs
import pprint

URL = 'https://news.ycombinator.com/'


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['Votes'], reverse=True)


def create_custom_hn(links_arg, subtext_arg):
    hn = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'Title': title, 'Link': href, 'Votes': points})
    return sort_by_votes(hn)


for page in range(1, 6):
    print(f'\nPage {page}, {URL}?p={page}')
    req = requests.get(f'{URL}?p={page}')

    soup = bs(req.text, 'html.parser')

    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')
    pprint.pprint(create_custom_hn(links, subtext))
